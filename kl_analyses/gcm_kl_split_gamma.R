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
mdir <- here("kl_analyses/mds_turtles_gcm_kl_gamma_split")
dir_create(mdir)

# SETTINGS ==========================================================================================
# vary c, gamma1, gamma2, and w here

input <- commandArgs(trailingOnly = T)
if(length(input)==0){
  params_0 <- c(.2,1,.75,.5)
}else{
  params_0 <- as.numeric(input)
}
# just need these for file naming
c_true <- params_0[1]
gamma_1_true <- params_0[2]
gamma_2_true <- params_0[3]
w_true <- params_0[4]
r <- 1 # city-block

# parameter ranges
c_min <- .01
gamma_1_min <- gamma_2_min <- .01
w_min <- .01

c_max <- 1
gamma_1_max <- gamma_2_max <- 1.5
w_max <- 1

# granularity of analysis
grain <- 20

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

n_trial <- 4 # NUMBER OF TRIALS
all_stim <- matrix(NA_real_,nrow=0,ncol=2)
for(i in 1:n_trial){
  all_stim <- rbind(all_stim,
                    A_exemplars, B_exemplars, test_stim)
}

# Preprocessing stimulus distances on each dimension ================================================================================================
n_stim_total <- nrow(all_stim)
n_A_exemplars <- nrow(A_exemplars)
n_B_exemplars <- nrow(B_exemplars)
A_exemplar_dists <- array(NA_real_,dim=c(n_stim_total,n_A_exemplars,2))
B_exemplar_dists <- array(NA_real_,dim=c(n_stim_total,n_B_exemplars,2))

for(s in 1:n_stim_total){
  print(s)
  for(a in 1:n_A_exemplars){
    A_exemplar_dists[s,a,] <- distance(all_stim[s,],A_exemplars[a,])
  }
  for(b in 1:n_B_exemplars){
    B_exemplar_dists[s,b,] <- distance(all_stim[s,],B_exemplars[b,])
  }
}

# setup for KL analysis ================================================================================================
ps <- glue("mds_turtles_kl_gamma_split_results_c={round(c_true,digits=3)}_gamma1={gamma_1_true}_gamma2={gamma_2_true}_w={w_true}_n_trial={n_trial}_grain={grain}")
f_kl <- path(mdir, glue("{ps}.RData"))

if(!file_exists(f_kl)){
  st <- Sys.time()
  kl <- gcm_kl_binomial_split_looper(params_0=params_0,
                                     params_min=c(c_min,gamma_1_min,
                                                gamma_2_min,
                                                w_min),
                                     params_max=c(c_max,gamma_1_max,
                                       gamma_2_max,
                                       w_max),
                                     grain=grain,
                                     A_exemplar_dists=A_exemplar_dists,
                                     B_exemplar_dists=B_exemplar_dists,
                                     r)
  end <- Sys.time()
  print(end-st)
  save(kl,file=f_kl)
}else{
  load(f_kl)
}
c_all <- seq(c_min,c_max,length.out=grain)
gamma_1_all <- seq(gamma_1_min,gamma_1_max,length.out=grain)
gamma_2_all <- seq(gamma_2_min,gamma_2_max,length.out=grain)
w_all <- seq(w_min,w_max,length.out=grain)
c_gamma_1_marginal <- apply(kl, c(1,2), mean)
c_gamma_1_marginal <- c_gamma_1_marginal/sum(c_gamma_1_marginal)
c_gamma_2_marginal <- apply(kl, c(1,3), mean)
c_gamma_2_marginal <- c_gamma_2_marginal/sum(c_gamma_2_marginal)

c_w_marginal <- apply(kl, c(1,4), mean)
c_w_marginal <- c_w_marginal/sum(c_w_marginal)

gamma_1_gamma_2_marginal <- apply(kl, c(2,3), mean)
gamma_1_gamma_2_marginal <- gamma_1_gamma_2_marginal/sum(gamma_1_gamma_2_marginal)

gamma_1_w_marginal <- apply(kl, c(2,4), mean)
gamma_1_w_marginal <- gamma_1_w_marginal/sum(gamma_1_w_marginal)
gamma_2_w_marginal <- apply(kl, c(3,4), mean)
gamma_2_w_marginal <- gamma_2_w_marginal/sum(gamma_2_w_marginal)

filled.contour(c_all,gamma_1_all,c_gamma_1_marginal,
               xlab="c",ylab=TeX("$\\gamma_{1}$"))
filled.contour(c_all,gamma_2_all,c_gamma_2_marginal,
               xlab="c",ylab=TeX("$\\gamma_{2}$"))
filled.contour(c_all,w_all,c_w_marginal,
               xlab="c",ylab="w")
filled.contour(gamma_1_all,gamma_2_all,gamma_1_gamma_2_marginal,
               xlab=TeX("$\\gamma_{1}$"),ylab=TeX("$\\gamma_{2}$"))
filled.contour(gamma_1_all,w_all,gamma_1_w_marginal,
               xlab=TeX("$\\gamma_{1}$"),ylab="w")
filled.contour(gamma_2_all,w_all,gamma_2_w_marginal,
               xlab=TeX("$\\gamma_{2}$"),ylab="w")

c_marginal <- apply(kl,1,mean)
c_marginal <- c_marginal/sum(c_marginal)
gamma_1_marginal <- apply(kl,2,mean)
gamma_1_marginal <- gamma_1_marginal/sum(gamma_1_marginal)
gamma_2_marginal <- apply(kl,3,mean)
gamma_2_marginal <- gamma_2_marginal/sum(gamma_2_marginal)
w_marginal <- apply(kl,4,mean)
w_marginal <- w_marginal/sum(w_marginal)

plot(c_all,c_marginal,type='l')
plot(gamma_1_all,gamma_1_marginal,type='l')
plot(gamma_2_all,gamma_2_marginal,type='l')
plot(w_all,w_marginal,type='l')

gamma_1_all[which.max(gamma_1_marginal)]
gamma_2_all[which.max(gamma_2_marginal)]
c_all[which.max(c_marginal)]
w_all[which.max(w_marginal)]
