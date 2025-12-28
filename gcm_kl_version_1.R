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
mdir <- here("mds_turtles_gcm_kl_version_1")
dir_create(mdir)

# set true params ==========================================================================================
c_true <- .1
gamma_true <- 1
w_true <- .5

r <- 1 # city-block
# Stim ================================================================================
get_exemplars <- function(mds,label){
  exemplars_1 <- mds_cat %>%
    filter(category==label) 
  # if(label=="Untrained"){
  #   exemplars_1 <- exemplars_1 %>%
  #     filter(stim %in% c(1,25))
  # }
  
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
inc <- .1

c_all <- seq(0,1,by=inc)
gamma_all <- seq(0,1.75,by=inc)
w_all <- seq(0,1,by=inc)

params_all <- expand_grid(c_all,gamma_all,w_all)
kl_results <- params_all
kl_results$kl <- numeric(nrow(kl_results))
n_pars <- nrow(params_all)

# KL Computation ================================================================================================
params_0 <- c("c"=c_true,
              "w"=w_true,
              "gamma"=gamma_true)
ps <- path(mdir,glue("mds_turtles_kl_version_1_results_c={round(c_true,digits=3)}_gamma={gamma_true}_w={w_true}_n_trial={n_trial}_inc={inc}"))
f_preds <- glue("{ps}.RData")
if(!file_exists(f_preds)){
  for(i in 1:n_pars){
    cat(i,"/",n_pars,"\n")
    kl_results$kl[i] <- gcm_kl(N=n_trial,
                                test=all_stim,
                                r=r,
                                A_exemplars=A_exemplars,
                                B_exemplars=B_exemplars,
                                params_1=c("c"=params_all$c_all[i],
                                           "gamma"=params_all$gamma_all[i],
                                           "w"=params_all$w_all[i]),
                                params_0=params_0)
  }
  save(kl_results,file=f_preds)
}else{
  load(f_preds)
}
# 
kl_results 
kl_results <- kl_results %>%
  rename(c=c_all,
         gamma=gamma_all,
         w=w_all)
max <- kl_results[which.max(kl_results$kl),]
max
kl_results %>%
  group_by(gamma,c) %>%
  summarise(kl=mean(kl)) %>%
  ungroup() %>%
  ggplot(aes(gamma,c,fill=kl))+
  geom_raster(interpolate = T)+
  scale_fill_gradient(name="")+
  labs(x=TeX("$\\gamma$"))+
  ggthemes::theme_few()
ggsave(filename = glue("{ps}_gamma_c.jpeg"),width=6,height=5,dpi=1200)

kl_results %>%
  group_by(c,w) %>%
  summarise(kl=mean(kl)) %>%
  ungroup() %>%
  ggplot(aes(c,w,fill=kl))+
  geom_raster(interpolate = T)+
  scale_fill_gradient(name="")+
  ggthemes::theme_few()
ggsave(filename = glue("{ps}_c_w.jpeg"),width=6,height=5,dpi=1200)

kl_results %>%
  group_by(gamma,w) %>%
  summarise(kl=mean(kl)) %>%
  ungroup() %>%
  ggplot(aes(gamma,w,fill=kl))+
  geom_raster(interpolate = T)+
  scale_fill_gradient(name="")+
  labs(x=TeX("$\\gamma$"))+
  ggthemes::theme_few()
ggsave(filename = glue("{ps}_gamma_w.jpeg"),width=6,height=5,dpi=1200)
# # 

# old ========================================================================
# params_0
# params_1 <- c("c"=0.1, "gamma"=1.7, "w"=0.5)
# p0 <- gcm_kl(N=n_trial, test=all_stim, r=r, A_exemplars=A_exemplars, B_exemplars=B_exemplars, params_0=params_0, params_1=params_0)
# p1 <- gcm_kl(N=n_trial, test=all_stim, r=r, A_exemplars=A_exemplars, B_exemplars=B_exemplars, params_0=params_0, params_1=params_1)
# p1
# p0
# which(p1>.99)
# 
# gcm_predict(all_stim[22,],params_1,r,A_exemplars,B_exemplars)
# gcm_predict(all_stim[22,],params_0,r,A_exemplars,B_exemplars)
# 
# gcm_predict(all_stim[23,],params_1,r,A_exemplars,B_exemplars)
# gcm_predict(all_stim[23,],params_0,r,A_exemplars,B_exemplars)
# 
# gcm_predict(all_stim[24,],params_1,r,A_exemplars,B_exemplars)
# gcm_predict(all_stim[24,],params_0,r,A_exemplars,B_exemplars)
