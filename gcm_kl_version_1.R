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
c_true <- .075
gamma_true <- 1
w_true <- .5

r <- 1 # city-block
# Stim ================================================================================
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
all_stim <- rbind(A_exemplars, B_exemplars, test_stim)

n_trial <- 4 # NUMBER OF TRIALS
# setup for KL analysis ================================================================================================
n_inc <- 60

# make sure that true parameter is in there
c_all <- seq(0.01,1,length.out=n_inc)
# if(!any(c_all==c_true)){
#   c_all <- c(c_all,c_true)
# }
gamma_all <- seq(0.01,2,length.out=n_inc)
# if(!any(gamma_all==gamma_true)){
#   gamma_all <- c(gamma_all,gamma_true)
# }
w_all <- seq(.01,.99,length.out=n_inc)
# if(!any(w_all==w_true)){
#   w_all <- c(w_all,w_true)
# }
params_all <- expand_grid(c_all,gamma_all,w_all)
n_pars <- nrow(params_all)

# KL Computation ================================================================================================
kl <- numeric(n_pars)
params_0 <- c("c"=c_true,
              "w"=w_true,
              "gamma"=gamma_true)
ps <- path(mdir,glue("mds_turtles_kl_version_1_results_c={round(c_true,digits=3)}_gamma={gamma_true}_w={w_true}_n_trial={n_trial}_n_inc={n_inc}"))
f_preds <- glue("{ps}.RData")
if(!file_exists(f_preds)){
  for(i in 1:n_pars){
    cat(i,"/",n_pars,"\n")
    kl[i] <- gcm_kl(N=n_trial,
                    test=all_stim,
                    r=r,
                    A_exemplars=A_exemplars,
                    B_exemplars=B_exemplars,
                    params_1=c("c"=params_all$c_all[i],
                               "gamma"=params_all$gamma_all[i],
                               "w"=params_all$w_all[i]),
                    params_0=params_0)
  }
  
  kl_results <- tibble(
    c=params_all$c_all,
    gamma=params_all$gamma_all,
    w=params_all$w_all,
    kl=kl
  )
  # add in true params just to verify
  kl_results <- bind_rows(
    kl_results,
    tibble(
      c=c_true,
      gamma=gamma_true,
      w=w_true,
      kl=gcm_kl(N=n_trial,
                 test=all_stim,
                 r=r,
                 A_exemplars=A_exemplars,
                 B_exemplars=B_exemplars,
                 params_1=c("c"=c_true,
                            "gamma"=gamma_true,
                            "w"=w_true),
                 params_0=params_0)
      
    )
  )
  save(kl_results,file=f_preds)
}else{
  load(f_preds)
}
# 
max <- kl_results[which.max(kl_results$kl),]

kl_results %>%
  group_by(gamma,c) %>%
  summarise(kl=sum(kl)) %>%
  ungroup() %>%
  filter(gamma!=gamma_true|c!=c_true) %>%
  ggplot(aes(gamma,c,fill=kl))+
  geom_raster(interpolate = T)+
  scale_fill_gradient(name="")+
  labs(x=TeX("$\\gamma$"))+
  ggthemes::theme_few()
ggsave(filename = glue("{ps}_gamma_c.jpeg"),width=6,height=5,dpi=1200)

kl_results %>%
  group_by(c,w) %>%
  summarise(kl=sum(kl)) %>%
  ungroup() %>%
  filter(w!=w_true|c!=c_true) %>%
  ggplot(aes(c,w,fill=kl))+
  geom_raster(interpolate = T)+
  scale_fill_gradient(name="")+
  ggthemes::theme_few()
ggsave(filename = glue("{ps}_c_w.jpeg"),width=6,height=5,dpi=1200)

kl_results %>%
  group_by(gamma,w) %>%
  summarise(kl=sum(kl)) %>%
  ungroup() %>%
  filter(w!=w_true|gamma!=gamma_true) %>%
  ggplot(aes(gamma,w,fill=kl))+
  geom_raster(interpolate = T)+
  scale_fill_gradient(name="")+
  labs(x=TeX("$\\gamma$"))+
  ggthemes::theme_few()
ggsave(filename = glue("{ps}_gamma_w.jpeg"),width=6,height=5,dpi=1200)
