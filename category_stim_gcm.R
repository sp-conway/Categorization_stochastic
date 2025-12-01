# set up ================================================================================
rm(list=ls())
library(here)
library(patchwork)
library(tidyverse)
library(glue)
library(fs)

# gcm functions
source(here("gcm_functions.R"))

# read in stimuli
mds_cat <- here("mds_turtles_categories_25_11/mds_orig_turtles_cat.csv") %>%
  read_csv()

# modeling dir
mdir <- here("mds_turtles_gcm_kl")
dir_create(mdir)
# set params ================================================================================
save_par <- T
c <- .075
w <- .5
gamma <- 1
b_A <- .5
r <- 1
params <- c("c"=c,"w"=w,"gamma"=gamma,"b_A"=b_A)
if(save_par){
  save(params,file=path(mdir,glue("params_set_{lubridate::today()}.RData")))
}

# set up for model ================================================================================
get_exemplars <- function(mds,label){
  exemplars_1 <- mds_cat %>%
    filter(category==label) 
  
  exemplars_2 <- exemplars_1 %>%
    select(angle_psy,radius_psy) %>%
    as.matrix()
  rownames(exemplars_2) <- exemplars_1$stim
  return(exemplars_2)
}

A_exemplars <- get_exemplars(mds_cat,"A")
B_exemplars <- get_exemplars(mds_cat,"B")
test_stim <- get_exemplars(mds,"Untrained")

n_exemplars <- nrow(A_exemplars) # I know they have the same number of rows, so just picked A
n_test <- nrow(test_stim)

p_train_A <- p_train_B <- numeric(n_exemplars)
names(p_train_A) <- rownames(A_exemplars)
names(p_train_B) <- rownames(B_exemplars)
p_test <- numeric(n_test)
names(p_test) <- rownames(test_stim)

# get model preds ======================================================================
for(i in 1:n_exemplars){
  p_train_A[i] <- gcm_predict(A_exemplars[i,],params,r,A_exemplars,B_exemplars)[1] # get model preds in terms of p(A)
  p_train_B[i] <- gcm_predict(B_exemplars[i,],params,r,A_exemplars,B_exemplars)[1]
}
for(i in 1:n_test){
  p_test[i] <- gcm_predict(test_stim[i,],params,r,A_exemplars,B_exemplars)[1]
}

preds <- tibble(
  stim=c(names(p_train_A),names(p_train_B),names(p_test)),
  p_A=c(p_train_A,p_train_B,p_test),
  category=c(rep("A",n_exemplars),rep("B",n_exemplars),rep("Untrained",n_test))
)
p_mds_cat <-  mds_cat %>%
  ggplot(aes(angle_psy,radius_psy,col=category))+
  geom_text(aes(label=stim),show.legend=F)+
  geom_point(alpha=0)+
  geom_abline(slope=1,intercept=0,linetype="dashed",alpha=.4)+
  ggsci::scale_color_futurama(name="Category")+
  labs(x="angle",y="radius")+
  coord_fixed(xlim=c(-50,50),ylim=c(-50,50))+
  ggthemes::theme_few()+
  theme(plot.title=element_text(hjust=0.5),
        legend.position="none")+
  guides(colour=guide_legend(override.aes=list(alpha=1)))
cat_preds <- preds %>%
  ggplot(aes(reorder(stim,-p_A),p_A,fill=category))+
  geom_col(position="dodge")+
  geom_text(aes(label=stim,y=p_A+.025))+
  geom_hline(yintercept=.5,linetype="dashed",alpha=.5)+
  labs(x="stimulus",y="p(A)")+
  scale_y_continuous(limits=c(0,1))+
  ggsci::scale_fill_futurama()+
  ggthemes::theme_few()+
  theme(legend.position=c(.8,.8))
p_both <- p_mds_cat|cat_preds
p_both
ggsave(p_mds_cat,filename=here("mds_turtles_categories_25_11/mds_turtle_cat_plot.jpeg"),
       width=4,height=4)
ggsave(p_both,filename=here("mds_turtles_categories_25_11/mds_turtle_cat_plot_gcm.jpeg"),
       width=12,height=4)
