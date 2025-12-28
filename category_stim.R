rm(list=ls())
library(here)
library(patchwork)
library(tidyverse)

mds <- here("mds_turtles/mds_turtles.csv") %>%
  read_csv()
orig <- here("mds_turtles/orig_turtles.csv") %>%
  read_csv()

source(here("gcm_functions.R"))

p_mds <- mds %>%
  ggplot(aes(angle,radius))+
  geom_text(aes(label=stim))+
  geom_abline(slope=1,intercept=0,linetype="dashed",alpha=.4)+
  labs(title="MDS")+
  coord_fixed(xlim=c(-50,50),ylim=c(-50,50))+
  ggthemes::theme_few()+
  theme(plot.title=element_text(hjust=0.5))
p_orig <- orig %>%
  ggplot(aes(angle,radius))+
  geom_text(aes(label=stim))+
  geom_abline(slope=-1,intercept=0,linetype="dashed",alpha=.4)+
  labs(title="Physical")+
  # coord_fixed(xlim=c(-50,50),ylim=c(-50,50))+
  ggthemes::theme_few()+
  theme(plot.title=element_text(hjust=0.5))
p_orig|p_mds

# categories ===============================================================
mds_cat <- mds %>%
  mutate(category=case_when(
    stim %in% c(1,7,13,19,25)~"Untrained",
    radius>angle ~ "A",
    angle>radius ~ "B"
  ))

plot_categories <- function(mds_cat){
  p_mds_cat <-  mds_cat %>%
    ggplot(aes(angle,radius,col=category))+
    geom_text(aes(label=stim),show.legend=F)+
    geom_point(alpha=0)+
    geom_abline(slope=1,intercept=0,linetype="dashed",alpha=.4)+
    ggsci::scale_color_futurama()+
    labs(title="MDS")+
    coord_fixed(xlim=c(-50,50),ylim=c(-50,50))+
    ggthemes::theme_few()+
    theme(plot.title=element_text(hjust=0.5),
          legend.position="bottom")+
    guides(colour=guide_legend(override.aes=list(alpha=1)))
  return(p_mds_cat)
}

p_mds_cat <- plot_categories(mds_cat)

mds_cat

A_exemplars <- mds_cat %>%
  filter(category=="A") %>%
  select(angle,radius) %>%
  as.matrix()

B_exemplars <- mds_cat %>%
  filter(category=="B") %>%
  select(angle,radius) %>%
  as.matrix()

test_stim <- mds_cat %>%
  filter(category=="Untrained") %>%
  select(angle,radius,stim) %>%
  as.matrix()

# testing gcm predictions =================================================
n_test <- nrow(test_stim)
ss <- matrix(NA, nrow=n_test, ncol=2)
p <- matrix(NA, nrow=n_test, ncol=1)
colnames(ss) <- c("A","B")
rownames(p) <- rownames(ss) <- test_stim[,3]
test_stim <- test_stim[,1:2]
c <- .05
gamma <- 3
b_A <- .5
r <- 1
w <- .5

params <- c("c"=c,
            "w"=w,
            "b_A"=b_A,
            "gamma"=gamma)
# for(i in 1:n_test){
#   ss[i,] <- gcm_predict(test_stim[i,], params, r, A_exemplars, B_exemplars, T)
#   p[i,] <- gcm_predict(test_stim[i,], params, r, A_exemplars, B_exemplars, F)
# }
# ss
# p
# write categories to file ============================================================
mds_cat_with_orig <- mds_cat %>% # join to physical stimulus values
  rename(angle_psy=angle,
         radius_psy=radius) %>%
  left_join(orig) 


write_csv(mds_cat_with_orig, file=here("mds_turtles_categories_25_11/mds_orig_turtles_cat.csv"))

  
