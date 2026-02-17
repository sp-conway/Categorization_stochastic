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
mdir <- here("kl_analyses/mds_turtles_gcm_kl_version_3_with_spearman")
dir_create(mdir)

# set true params ==========================================================================================
# vary c, gamma1, gamma2, and w here

input <- commandArgs(trailingOnly = T)
if(length(input)==0){
  params <- c(.2,1,.75,.5)
}else{
  params <- as.numeric(input)
}
c_true <- params[1]
gamma_1_true <- params[2]
gamma_2_true <- params[3]
w_true <- params[4]
# print(params_num)


# bias is fixed, so is r
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
inc <- .1

c_all <- seq(0,1,by=inc)
gamma_1_all <- seq(0,1.5,by=inc)
gamma_2_all <- seq(0,1.5,by=inc)
w_all <- seq(0,1,by=inc)

# params_all <- expand_grid(c_all,gamma_1_all,gamma_2_all,w_all)
# kl_results <- params_all
# kl_results$kl <- numeric(nrow(kl_results))
# n_pars <- nrow(params_all)
# n_bias <- length(b_A)

# KL Computation ================================================================================================
n_c <- length(c_all)
n_g1 <- length(gamma_1_all)
n_g2 <- length(gamma_2_all)
n_w <- length(w_all)

ps <- glue("mds_turtles_kl_version_3_results_c={round(c_true,digits=3)}_gamma1={gamma_1_true}_gamma2={gamma_2_true}_w={w_true}_n_trial={n_trial}_inc={inc}")
f_kl <- path(mdir, glue("{ps}.RData"))
# f_kl_sp <- path(mdir, glue("{ps}_spearman.RData"))

if(!file_exists(f_kl)){
  kl <- array(NA_real_,dim=c(n_c,n_g1,n_g2,n_w))
  for(c in 1:n_c){
    for(g1 in 1:n_g1){
      for(g2 in 1:n_g2){
        for(w in 1:n_w){
          cat(c,"/",n_c,"\n",
              g1,"/",n_g1,"\n",
              g2,"/",n_g2,"\n",
              w,"/",n_w,"\n")
          kl[c,g1,g2,w] <- gcm_kl(N=n_trial,
                                        test=all_stim,
                                        r=r,
                                        A_exemplars=A_exemplars,
                                        B_exemplars=B_exemplars,
                                        params_1=c("c"=c_all[c],
                                                   "gamma"=gamma_1_all[g1],
                                                   "w"=w_all[w]),
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
                                       params_1=c("c"=c_all[c],
                                                  "gamma"=gamma_2_all[g2],
                                                  "w"=w_all[w]),
                                       params_0=c(
                                         "c"=c_true,
                                         "w"=w_true,
                                         "gamma"=gamma_2_true
                                       ))
        }
      }
    }
  }
  save(kl,file=f_kl)
  # inds <- 1:4
  # kl_sp <- matrix(NA, nrow=length(inds), ncol=length(inds))
  # row.names(kl_sp) <- c("c","gamma_1","gamma_2","w")
  # colnames(kl_sp) <- c("c","gamma_1","gamma_2","w")
  # for(i in inds){
  #   for(j in inds){
  #     cum1 <- apply(kl,c(inds[which(inds!=i)]),cumsum)
  #     # cum1 <- cum1/sum(cum1)#as.vector(cum1/sum(cum1))
  #     
  #     cum2 <- apply(kl,c(inds[which(inds!=j)]),cumsum)
  #     # cum2 <- cum2/sum(cum2)#as.vector(cum2/sum(cum2))
  #     kl_sp[i,j] <- cor(cum1,cum2,method="spearman")
  #   }
  # }
  
  # convert to tidy data frame for easier vis. This is slow
  kl_n_row <- length(c_all)*length(gamma_1_all)*length(gamma_2_all)*length(w_all)
  kl_df <- tibble(
    c=numeric(kl_n_row),
    gamma_1=numeric(kl_n_row),
    gamma_2=numeric(kl_n_row),
    w=numeric(kl_n_row),
    kl=numeric(kl_n_row),
  )
  i <- 1
  for(c in 1:n_c){
    for(g1 in 1:n_g1){
      for(g2 in 1:n_g2){
        for(w in 1:n_w){
          print(i)
          kl_df$c[i] <- c_all[c]
          kl_df$gamma_1[i] <- gamma_1_all[g1]
          kl_df$gamma_2[i] <- gamma_2_all[g2]
          kl_df$w[i] <- w_all[w]
          kl_df$kl[i] <- kl[c,g1,g2,w]
          i <- i+1
        }
      }
    }
  }
  save(kl,kl_df,file=f_kl)
}else{
  load(f_kl)
}

# c_g1_marginal <- apply(kl, c(1,3), FUN=mean)
# c_g1_marginal <- c_g1_marginal/sum(c_g1_marginal)
# filled.contour(c_g1_marginal)
# 
# par(mfrow=c(3,2))
# 

gamma1_c_plot <- kl_df %>%
  group_by(gamma_1,c) %>%
  summarise(kl=mean(kl)) %>%
  ungroup() %>%
  # mutate(kl=kl/sum(kl)) %>%
  ggplot(aes(gamma_1,c,fill=kl))+
  geom_raster(interpolate=F)+
  geom_vline(xintercept=gamma_1_true,linetype="dashed",col="red",alpha=.5)+
  geom_hline(yintercept=c_true,linetype="dashed",col="red",alpha=.5)+
  scale_fill_viridis_c(name="")+
  coord_fixed(xlim=c(0,1.5),ylim=c(0,1))+
  labs(x=TeX("$\\gamma_{1}$"),y="c")+#,
       #subtitle = TeX(paste0("Spearman's $\\rho=",
       #                     round(kl_sp["c","gamma_1"],digits=3),"$")))+
  ggthemes::theme_few()+
  theme(plot.subtitle = element_text(hjust=0))
gamma1_c_plot
gamma2_c_plot <- kl_df %>%
  group_by(gamma_2,c) %>%
  summarise(kl=mean(kl)) %>%
  ungroup() %>%
  # mutate(kl=kl/sum(kl)) %>%
  ggplot(aes(gamma_2,c,fill=kl))+
  geom_raster(interpolate=F)+
  geom_vline(xintercept=gamma_2_true,linetype="dashed",col="red",alpha=.5)+
  geom_hline(yintercept=c_true,linetype="dashed",col="red",alpha=.5)+
  scale_fill_viridis_c(name="")+
  coord_fixed(xlim=c(0,1.5),ylim=c(0,1))+
  labs(x=TeX("$\\gamma_{2}$"),y="c")+
       # subtitle = TeX(paste0("Spearman's $\\rho=",
       #                      round(kl_sp["c","gamma_2"],digits=3),"$")))+
  ggthemes::theme_few()+
  theme(plot.subtitle = element_text(hjust=0))
gamma2_c_plot
# # 
gamma2_w_plot <- kl_df %>%
  group_by(gamma_2,w) %>%
  summarise(kl=mean(kl)) %>%
  ungroup() %>%
  # mutate(kl=kl/sum(kl)) %>%
  ggplot(aes(gamma_2,w,fill=kl))+
  geom_raster(interpolate=F)+
  geom_vline(xintercept=gamma_2_true,linetype="dashed",col="red",alpha=.5)+
  geom_hline(yintercept=w_true,linetype="dashed",col="red",alpha=.5)+
  scale_fill_viridis_c(name="")+
  coord_fixed(xlim=c(0,1.5),ylim=c(0,1))+
  labs(x=TeX("$\\gamma_{2}$"),y="w")+
       # subtitle = TeX(paste0("Spearman's $\\rho=",
       #                      round(kl_sp["gamma_2","w"],digits=3),"$")))+
  ggthemes::theme_few()+
  theme(plot.subtitle = element_text(hjust=0))
# # 
gamma1_w_plot <- kl_df %>%
  group_by(gamma_1,w) %>%
  summarise(kl=mean(kl)) %>%
  ungroup() %>%
  # mutate(kl=kl/sum(kl)) %>%
  ggplot(aes(gamma_1,w,fill=kl))+
  geom_raster(interpolate=F)+
  geom_vline(xintercept=gamma_1_true,linetype="dashed",col="red",alpha=.5)+
  geom_hline(yintercept=w_true,linetype="dashed",col="red",alpha=.5)+
  scale_fill_viridis_c(name="")+
  coord_fixed(xlim=c(0,1.5),ylim=c(0,1))+
  labs(x=TeX("$\\gamma_{1}$"),y="w")+
       # subtitle = TeX(paste0("Spearman's $\\rho=",
       #                      round(kl_sp["gamma_1","w"],digits=3),"$")))+
  ggthemes::theme_few()+
  theme(plot.subtitle = element_text(hjust=0))
# # 
# # 
c_w_plot <- kl_df %>%
  group_by(c,w) %>%
  summarise(kl=mean(kl)) %>%
  ungroup() %>%
  # mutate(kl=kl/sum(kl)) %>%
  ggplot(aes(c,w,fill=kl))+
  geom_raster(interpolate=F)+
  geom_vline(xintercept=c_true,linetype="dashed",col="red",alpha=.5)+
  geom_hline(yintercept=w_true,linetype="dashed",col="red",alpha=.5)+
  scale_fill_viridis_c(name="")+
  coord_fixed(xlim=c(0,1),ylim=c(0,1))+
  labs(x="c",y="w")+#,
       # subtitle = TeX(paste0("Spearman's $\\rho=",
       #                      round(kl_sp["c","w"],digits=3),"$")))+
  ggthemes::theme_few()+
  theme(plot.subtitle = element_text(hjust=0))
# # 
# # 
gamma1_gamma2_plot <- kl_df %>%
  group_by(gamma_1,gamma_2) %>%
  summarise(kl=mean(kl)) %>%
  ungroup() %>%
  # mutate(kl=kl/sum(kl)) %>%
  ggplot(aes(gamma_1, gamma_2,fill=kl))+
  geom_raster(interpolate=F)+
  geom_vline(xintercept=gamma_1_true,linetype="dashed",col="red",alpha=.5)+
  geom_hline(yintercept=gamma_2_true,linetype="dashed",col="red",alpha=.5)+
  scale_fill_viridis_c(name="")+
  coord_fixed(xlim=c(0,1.5),
              ylim=c(0,1.5))+
  labs(x=TeX("$\\gamma_{1}$"),y=TeX("$\\gamma_{2}$"))+#,
       # subtitle = TeX(paste0("Spearman's $\\rho=",
       #                      round(kl_sp["gamma_2","gamma_1"],digits=3),"$")))+
  ggthemes::theme_few()+
  theme(plot.subtitle = element_text(hjust=0))
# # 
all_plot <-(gamma1_c_plot +
              gamma2_c_plot+
              gamma1_w_plot+
              gamma2_w_plot+
              c_w_plot+
              gamma1_gamma2_plot)+
  plot_layout(ncol=2,nrow=3,guides = "collect",byrow=T,widths=rep(1,6),heights=rep(1,6))+
  patchwork::plot_annotation(theme=theme(text=element_text(size=15),
                                         plot.caption = element_text(hjust=0)),
                            caption = "Dashed red lines mark true parameter values.")
all_plot
# kl_sp
ggsave(all_plot,filename=path(mdir,glue("{ps}.jpeg")),width=8,height=10)
ggsave(all_plot,filename=path(mdir,glue("{ps}.pdf")),width=8,height=10)


kl_df %>%
  group_by(c) %>%
  summarise(kl=mean(kl)) %>%
  ungroup() %>%
  ggplot(aes(c,kl))+
  geom_path()

kl_df %>%
  group_by(gamma_1) %>%
  summarise(kl=mean(kl)) %>%
  ungroup() %>%
  arrange(desc(kl))
  ggplot(aes(gamma_1,kl))+
  geom_path()

kl_df %>%
  group_by(gamma_2) %>%
  summarise(kl=mean(kl)) %>%
  ungroup() %>%
  arrange(desc(kl))
  ggplot(aes(gamma_2,kl))+
  geom_path()

kl_df %>%
  group_by(w) %>%
  summarise(kl=mean(kl)) %>%
  ungroup() %>%
  ggplot(aes(w,kl))+
  geom_path()
# spearman rho ========================================================================================================================
# 
# 
# 
# for(c in c_all){
#   for(g1 in gamma_1_all){
#     for(g2 in gamma_2_all){
#       for(w in w_all){
#         kl_array
#       }
#     }
#   }
# }
