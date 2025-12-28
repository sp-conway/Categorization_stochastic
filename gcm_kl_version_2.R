# set up ================================================================================
rm(list=ls())
library(here)
library(patchwork)
library(tidyverse)
library(glue)
library(fs)
library(latex2exp)

# gcm functions
source(here("gcm_functions.R"))
source(here("kl_functions.R"))

# read in stimuli
mds_cat <- here("mds_turtles_categories_25_11/mds_orig_turtles_cat.csv") %>%
  read_csv() 
mdir <- here("mds_turtles_gcm_kl_version_2")
dir_create(mdir)

# set true params ==========================================================================================
c_true <- .1
gamma_true <- 1
w_true <- .5
b_A <- c(.1, .3, .5, .7, .9)

r <- 1 # city-block
# Stim ================================================================================
get_exemplars <- function(mds,label){
  exemplars_1 <- mds_cat %>%
    filter(category==label) 
  # if(label=="Untrained"){
  #   exemplars_1 <- exemplars_1 %>%
  #     filter(stim %in% c(1,25))
  # }
  # 
  exemplars_2 <- exemplars_1 %>%
    select(angle_psy,radius_psy) %>%
    as.matrix()
  rownames(exemplars_2) <- exemplars_1$stim
  return(exemplars_2)
}

A_exemplars <- get_exemplars(mds_cat,"A")
B_exemplars <- get_exemplars(mds_cat,"B")
test_stim <- get_exemplars(mds,"Untrained")
all_stim <- rbind(A_exemplars, B_exemplars, test_stim)

n_trial <- 4 # NUMBER OF TRIALS
# setup for KL analysis ================================================================================================
inc <- .05

c_all <- seq(0,1,by=inc)
gamma_all <- seq(0,2,by=inc)
w_all <- seq(0,1,by=inc)

params_all <- expand_grid(c_all,gamma_all,w_all)
kl_results <- params_all
kl_results$kl <- numeric(nrow(kl_results))
n_pars <- nrow(params_all)
n_bias <- length(b_A)

# KL Computation ================================================================================================
kl <- matrix(NA_real_,nrow=n_pars,ncol=n_bias)

ps <- path(mdir,glue("mds_turtles_kl_version_2_results_c={round(c_true,digits=3)}_gamma={gamma_true}_w={w_true}_n_trial={n_trial}_inc={inc}"))
f_preds <- glue("{ps}.RData")
if(!file_exists(f_preds)){
  for(i in 1:n_pars){
    cat(i,"/",n_pars,"\n")
    for(j in 1:n_bias){
      # cat(j,"/",n_pars,"\n")
      params_0 <- c("c"=c_true,
                    "w"=w_true,
                    "gamma"=gamma_true,
                    "b_A"=b_A[j])
      kl[i,j] <- gcm_kl(N=n_trial,
                        test=all_stim,
                        r=r,
                        A_exemplars=A_exemplars,
                        B_exemplars=B_exemplars,
                        params_1=c("c"=params_all$c_all[i],
                                   "gamma"=params_all$gamma_all[i],
                                   "w"=params_all$w_all[i],
                                   "b_A"=b_A[j]),
                        params_0=params_0)
    }
  }
  save(kl,file=f_preds)
}else{
  load(f_preds)
}

colnames(kl) <- as.character(b_A)
kl_1 <- as_tibble(cbind(kl,as.matrix(params_all))) %>%
  pivot_longer(contains("."),names_to = "b_A",
               values_to = "kl") %>%
  rename(c=c_all,
         gamma=gamma_all,
         w=w_all) %>%
  mutate(b_A=as.numeric(b_A))
# 
# marg_kl <- function(dat,bias,vars_pair){
#   vars_pair <- unlist(vars_pair)
#   x <- dat %>%
#     nest(.by = b_A) %>%
#     mutate(m=map(data, function(data) data %>% group_by(across({{vars_pair}})) %>% summarise(kl=mean(kl)) %>% ungroup() %>%
#                     mutate(pair=str_glue("{vars_pair[1]}-{vars_pair[2]}"))))
#   x$m[[1]]$b_A <- .1
#   x$m[[2]]$b_A <- .3
#   x$m[[3]]$b_A <- .5
#   x$m[[4]]$b_A <- .7
#   x$m[[5]]$b_A <- .9
#    x %>%
#      select(m) %>%
#      unnest(m)
# }
# 
# 
# combos <- expand_grid(
#   b_A,
#   vars_pair=list(c("c","gamma"),
#                  c("c","w"),
#                  c("gamma","w")),
# ) 
# 
# kl_all <- map(1:nrow(combos),~marg_kl(kl_1,combos$b_A[.x],combos$vars_pair[.x])) %>%
#   list_rbind()

kl_1 %>%
  filter(w==w_true) %>%
  group_by(c, gamma, b_A) %>%
  summarise(kl=sum(kl)) %>%
  ungroup() %>%
  ggplot(aes(gamma,c,fill=kl))+
  geom_raster(interpolate = T)+
  scale_fill_gradient(name="")+
  coord_fixed(xlim=c(0,2),ylim=c(0,1))+
  facet_grid(vars(b_A))+
  labs(x=TeX("$\\gamma$"))+
  ggthemes::theme_few()
ggsave(filename=glue("{ps}_c_gamma.jpeg"),dpi=1200,
       width=4,height=4)


kl_1 %>%
  filter(gamma==gamma_true) %>%
  group_by(c,w) %>%
  summarise(kl=sum(kl)) %>%
  ungroup() %>%
  ggplot(aes(c,w,fill=kl))+
  geom_raster(interpolate = T)+
  scale_fill_gradient(name="")+
  coord_fixed(xlim=c(0,1),ylim=c(0,1))+
  # facet_grid(vars(b_A))+
  # labs(x=TeX("$\\gamma$"))+
  ggthemes::theme_few()
ggsave(filename=glue("{ps}_c_w.jpeg"),dpi=1200,
       width=4,height=4)

kl_1 %>%
  filter(c==c_true) %>%
  group_by(gamma,w) %>%
  summarise(kl=sum(kl)) %>%
  ungroup() %>%
  ggplot(aes(gamma,w,fill=kl))+
  geom_raster(interpolate = T)+
  scale_fill_gradient(name="")+
  coord_fixed(xlim=c(0,2),ylim=c(0,1))+
  labs(x=TeX("$\\gamma$"))+
  ggthemes::theme_few()
ggsave(filename=glue("{ps}_gamma_w.jpeg"),dpi=1200,
       width=4,height=4)


kl_1[which.max(kl_1$kl),]
