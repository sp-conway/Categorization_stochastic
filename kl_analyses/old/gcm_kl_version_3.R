# set up ================================================================================
rm(list=ls())
library(here)
library(patchwork)
library(tidyverse)
library(glue)
library(fs)
library(latex2exp)
library(akima)

# gcm functions
source(here("kl_analyses","gcm_functions.R"))
source(here("kl_analyses","kl_functions.R"))

# read in stimuli
mds_cat <- here("kl_analyses/mds_turtles_categories_25_11/mds_orig_turtles_cat.csv") %>%
  read_csv() 
mdir <- here("kl_analyses/mds_turtles_gcm_kl_version_3")
dir_create(mdir)

# set true params ==========================================================================================
c_true <- .2
gamma_1_true <- 1
gamma_2_true <- .75
w_true <- .5
b_A <- .5

r <- 1 # city-block
# Stim ================================================================================
get_exemplars <- function(mds_cat,label){
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
test_stim <- get_exemplars(mds_cat,"Untrained")
all_stim <- rbind(A_exemplars, B_exemplars, test_stim)

n_trial <- 4 # NUMBER OF TRIALS
# setup for KL analysis ================================================================================================
inc <- .05

c_all <- seq(0,1,by=inc)
gamma_1_all <- seq(0,1.5,by=inc)
gamma_2_all <- seq(0,1.5,by=inc)
w_all <- seq(0,1,by=inc)

params_all <- expand_grid(c_all,gamma_1_all,gamma_2_all,w_all)
kl_results <- params_all
kl_results$kl <- numeric(nrow(kl_results))
n_pars <- nrow(params_all)
n_bias <- length(b_A)

# KL Computation ================================================================================================
kl <- numeric(n_pars)

ps <- glue("mds_turtles_kl_version_3_results_c={round(c_true,digits=3)}_gamma1={gamma_1_true}_gamma2={gamma_2_true}_w={w_true}_n_trial={n_trial}_inc={inc}")
f_preds <- path(mdir, glue("{ps}.RData"))
if(!file_exists(f_preds)){
  for(i in 1:n_pars){
    cat(i,"/",n_pars,"\n")
    kl[i] <- gcm_kl(N=n_trial,
                      test=all_stim,
                      r=r,
                      A_exemplars=A_exemplars,
                      B_exemplars=B_exemplars,
                      params_1=c("c"=params_all$c_all[i],
                                 "gamma"=params_all$gamma_1_all[i],
                                 "w"=params_all$w_all[i],
                                 "b_A"=b_A),
                      params_0=c(
                        "c"=c_true,
                        "w"=w_true,
                        "gamma"=gamma_1_true
                      ))+
      gcm_kl(N=n_trial,
                       test=all_stim,
                       r=r,
                       A_exemplars=A_exemplars,
                       B_exemplars=B_exemplars,
                       params_1=c("c"=params_all$c_all[i],
                                  "gamma"=params_all$gamma_2_all[i],
                                  "w"=params_all$w_all[i],
                                  "b_A"=b_A),
                       params_0=c(
                         "c"=c_true,
                         "w"=w_true,
                         "gamma"=gamma_2_true
                       ))
  }
  save(kl,file=f_preds)
}else{
  load(f_preds)
}

# 
kl_1 <- params_all %>%
  mutate(kl=kl) %>%
  rename(c=c_all,
         gamma_1=gamma_1_all,
         gamma_2=gamma_2_all,
         w=w_all)


gamma1_c_plot <- kl_1 %>%
  group_by(gamma_1,c) %>%
  summarise(kl=mean(kl)) %>%
  ungroup() %>%
  ggplot(aes(gamma_1,c,fill=kl))+
  geom_raster(interpolate=F)+
  scale_fill_viridis_c(name="")+
  coord_fixed(xlim=c(0,1.5),ylim=c(0,1))+
  labs(x=TeX("$\\gamma_{1}$"))+
  ggthemes::theme_few()

gamma2_c_plot <- kl_1 %>%
  group_by(gamma_2,c) %>%
  summarise(kl=mean(kl)) %>%
  ungroup() %>%
  ggplot(aes(gamma_2,c,fill=kl))+
  geom_raster(interpolate=F)+
  scale_fill_viridis_c(name="")+
  labs(x=TeX("$\\gamma_{2}$"))+
  coord_fixed(xlim=c(0,1.5),ylim=c(0,1))+
  ggthemes::theme_few()
# 
gamma2_w_plot <- kl_1 %>%
  group_by(gamma_2,w) %>%
  summarise(kl=mean(kl)) %>%
  ungroup() %>%
  ggplot(aes(gamma_2,w,fill=kl))+
  geom_raster(interpolate=F)+
  scale_fill_viridis_c(name="")+
  coord_fixed(xlim=c(0,1.5),ylim=c(0,1))+
  labs(x=TeX("$\\gamma_{2}$"))+
  ggthemes::theme_few()
# 
gamma1_w_plot <- kl_1 %>%
  group_by(gamma_1,w) %>%
  summarise(kl=mean(kl)) %>%
  ungroup() %>%
  ggplot(aes(gamma_1,w,fill=kl))+
  geom_raster(interpolate=F)+
  scale_fill_viridis_c(name="")+
  coord_fixed(xlim=c(0,1.5),ylim=c(0,1))+
  labs(x=TeX("$\\gamma_{1}$"))+
  ggthemes::theme_few()
# 
# 
c_w_plot <- kl_1 %>%
  group_by(c,w) %>%
  summarise(kl=mean(kl)) %>%
  ungroup() %>%
  ggplot(aes(c,w,fill=kl))+
  geom_raster(interpolate=F)+
  scale_fill_viridis_c(name="")+
  coord_fixed(xlim=c(0,1),ylim=c(0,1))+
  ggthemes::theme_few()
# 
# 
gamma1_gamma2_plot <- kl_1 %>%
  group_by(gamma_1,gamma_2) %>%
  summarise(kl=mean(kl)) %>%
  ungroup() %>%
  ggplot(aes(gamma_1, gamma_2,fill=kl))+
  geom_raster(interpolate=F)+
  scale_fill_viridis_c(name="")+
  labs(x=TeX("$\\gamma_{1}$"),y=TeX("$\\gamma_{2}$"))+
  coord_fixed(xlim=c(0,1.5),ylim=c(0,1.5))+
  ggthemes::theme_few()
# 
all_plot <-(gamma1_c_plot +
  gamma2_c_plot+
  gamma1_w_plot+
  gamma2_w_plot+
  c_w_plot+
  gamma1_gamma2_plot)+
  plot_layout(ncol=2,nrow=3,guides = "collect",byrow=T,widths=rep(1,6),heights=rep(1,6))+
  patchwork::plot_annotation(theme=theme(text=element_text(size=15)))
all_plot
ggsave(all_plot,filename=path(mdir,glue("{ps}.jpeg")),width=8,height=10)
ggsave(all_plot,filename=path(mdir,glue("{ps}.pdf")),width=8,height=10)

