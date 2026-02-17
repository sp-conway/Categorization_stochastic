# set up ================================================================================
rm(list=ls())
library(here)
library(patchwork)
library(tidyverse)
library(glue)
library(fs)
library(latex2exp)

# gcm functions
source(here("kl_analyses","gcm_functions.R"))
source(here("kl_analyses","kl_functions.R"))

# read in stimuli
mds_cat <- here("kl_analyses/mds_turtles/mds_turtles.csv") %>%
  read_csv() %>%
  mutate(category=case_when(
    stim %in% c(1,7,13,19,25)~"Untrained",
    radius>angle ~ "A",
    angle>radius ~ "B"
  ))

# load parameters
mdir <- here("kl_analyses/mds_turtles_gcm_kl")
f_params <- dir_ls(mdir,regexp = ".RData") %>%
  sort(decreasing=T) # read in most recent param set
load(f_params[1])

params_true <- c(params["c"],params["gamma"]) # only need these two here
c_true <- params["c"]
gamma_true <- params["gamma"]

r <- 1 # city-block
# Stim ================================================================================
get_exemplars <- function(mds,label){
  exemplars_1 <- mds_cat %>%
    filter(category==label) 
  
  exemplars_2 <- exemplars_1 %>%
    select(angle,radius) %>%
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
inc <- .025
c_all <- seq(0.01,1.5,inc)
gamma_all <- seq(0.01,4,inc)
params_all <- expand_grid(c_all,gamma_all)

params_all_check <- params_all %>%
  filter(c_all==c_true & gamma_all==gamma_true)

if(nrow(params_all_check)==0){
  params_all <- params_all %>%
    bind_rows(
      tibble(c_all=c_true,
             gamma_all=gamma_true) # also add in true param values if needed
    )
}
  

n_pars <- nrow(params_all)

# KL Computation ================================================================================================
kl <- numeric(n_pars)
params_0 <- params_true
names(params_0) <- c("c","gamma")
ps <- path(mdir,glue("mds_turtles_kl_results_c={round(c_true,digits=3)}_gamma={gamma_true}_n_trial={n_trial}_inc={inc}"))
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
                               "gamma"=params_all$gamma_all[i]),
                    params_0=params_0)
  }
  
  kl_results <- tibble(
    c=params_all$c_all,
    gamma=params_all$gamma_all,
    # kl_logged=kl,
    # kl=exp(kl)
    kl=kl
  )
  save(kl_results,file=f_preds)
}else{
  load(f_preds)
}

max <- kl_results[which.max(kl_results$kl),] # verifying that true params have highest likelihood
c_r <- range(c_all)
g_r <- range(gamma_all)
kl_results %>%
  filter(c!=c_true | gamma!=gamma_true) %>%
  ggplot(aes(c,gamma,fill=kl))+
  geom_raster(interpolate = T)+
  # geom_vline(xintercept=c_true,linetype="dashed",col="red",linewidth=.45,alpha=.5)+
  # geom_hline(yintercept=gamma_true,linetype="dashed",col="red",linewidth=.45,alpha=.5)+
  # geom_hline(yintercept=1,linetype="dashed",col="white",linewidth=.45)+
  geom_point(data=max,aes(c,gamma),shape="X",size=2.5,col="red")+
  # coord_fixed(xlim=c(c_r[1],c_r[2]),ylim=c(g_r[1],g_r[2]))+
  labs(x="c",y=TeX("$\\gamma$"))+
  ggthemes::theme_few()+
  theme(legend.position = "none")
ggsave(filename=here(glue("{ps}.jpeg")),width=4,height=4)
