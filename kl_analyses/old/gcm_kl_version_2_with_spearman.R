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
mdir <- here("kl_analyses/mds_turtles_gcm_kl_version_2_with_spearman")
dir_create(mdir)

# set true params ==========================================================================================
c_true <- .2
gamma_true <- .75
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
n_inc <- 20

c_all <- seq(0,1,length.out=n_inc)
gamma_all <- seq(0,1.5,length.out=n_inc)
w_all <- seq(0,1,length.out=n_inc)

# params_all <- expand_grid(c_all,gamma_1_all,gamma_2_all,w_all)
# kl_results <- params_all
# kl_results$kl <- numeric(nrow(kl_results))
# n_pars <- nrow(params_all)
# n_bias <- length(b_A)

# KL Computation ================================================================================================
n_c <- length(c_all)
n_gamma <- length(gamma_all)
n_w <- length(w_all)

kl <- array(NA_real_,dim=c(n_c,n_gamma,n_w))


ps <- glue("mds_turtles_kl_version_3_results_c={round(c_true,digits=3)}_gamma={gamma_true}_w={w_true}_n_trial={n_trial}_n_inc={n_inc}")
f_kl <- path(mdir, glue("{ps}.RData"))
f_kl_sp <- path(mdir, glue("{ps}_spearman.RData"))
if(!file_exists(f_kl)){
  
  for(c in 1:n_c){
    for(g in 1:n_gamma){
      for(w in 1:n_w){
        cat(c,"/",n_c,"\n",
            g,"/",n_gamma,"\n",
            w,"/",n_w,"\n")
        kl[c,g,w] <- gcm_kl(N=n_trial,
                            test=all_stim,
                            r=r,
                            A_exemplars=A_exemplars,
                            B_exemplars=B_exemplars,
                            params_1=c("c"=c_all[c],
                                       "gamma"=gamma_all[g],
                                       "w"=w_all[w],
                                       "b_A"=b_A),
                            params_0=c(
                              "c"=c_true,
                              "w"=w_true,
                              "gamma"=gamma_true
                            ))
      }
    }
  }
  
  inds <- 1:3
  kl_sp <- matrix(NA, nrow=length(inds), ncol=length(inds))
  row.names(kl_sp) <- c("c","gamma","w")
  colnames(kl_sp) <- c("c","gamma","w")
  for(i in inds){
    for(j in inds){
      cum1 <- apply(kl,c(inds[which(inds!=i)]),cumsum)
      # cum1 <- cum1/sum(cum1)#as.vector(cum1/sum(cum1))
      
      cum2 <- apply(kl,c(inds[which(inds!=j)]),cumsum)
      # cum2 <- cum2/sum(cum2)#as.vector(cum2/sum(cum2))
      kl_sp[i,j] <- cor(cum1,cum2,method="spearman")
    }
  }
  kl_df <- tibble(
    c=numeric(n_inc^3),
    gamma=numeric(n_inc^3),
    w=numeric(n_inc^3),
    kl=numeric(n_inc^3),
  )
  i <- 1
  for(c in 1:n_c){
    for(g in 1:n_gamma){
      for(w in 1:n_w){
        print(i)
        kl_df$c[i] <- c_all[c]
        kl_df$gamma[i] <- gamma_all[g]
        kl_df$w[i] <- w_all[w]
        kl_df$kl[i] <- kl[c,g,w]
        i <- i+1
      }
    }
  }
  save(kl,kl_df,file=f_kl)
  save(kl_sp,file=f_kl_sp)
}else{
  load(f_kl)
  load(f_kl_sp)
}



gamma_c_plot <- kl_df %>%
  group_by(gamma,c) %>%
  summarise(kl=mean(kl)) %>%
  ungroup() %>%
  ggplot(aes(gamma,c,fill=kl))+
  geom_raster(interpolate=F)+
  geom_vline(xintercept=gamma_true,linetype="dashed",col="red",alpha=.5)+
  geom_hline(yintercept=c_true,linetype="dashed",col="red",alpha=.5)+
  scale_fill_viridis_c(name="")+
  coord_fixed(xlim=c(0,1.5),ylim=c(0,1))+
  labs(x=TeX("$\\gamma$"),y="c",
       subtitle = TeX(paste0("Spearman's $\\rho=",
                             round(kl_sp["c","gamma"],digits=3),"$")))+
  ggthemes::theme_few()+
  theme(plot.subtitle = element_text(hjust=0))
  ggthemes::theme_few()

gamma_w_plot <- kl_df %>%
  group_by(gamma,w) %>%
  summarise(kl=mean(kl)) %>%
  ungroup() %>%
  ggplot(aes(gamma,w,fill=kl))+
  geom_raster(interpolate=F)+
  geom_vline(xintercept=gamma_true,linetype="dashed",col="red",alpha=.5)+
  geom_hline(yintercept=w_true,linetype="dashed",col="red",alpha=.5)+
  scale_fill_viridis_c(name="")+
  coord_fixed(xlim=c(0,1.5),ylim=c(0,1))+
  labs(x=TeX("$\\gamma$"),y="w",
       subtitle = TeX(paste0("Spearman's $\\rho=",
                             round(kl_sp["w","gamma"],digits=3),"$")))+
  ggthemes::theme_few()+
  theme(plot.subtitle = element_text(hjust=0))

c_w_plot <- kl_df %>%
  group_by(c,w) %>%
  summarise(kl=mean(kl)) %>%
  ungroup() %>%
  ggplot(aes(c,w,fill=kl))+
  geom_raster(interpolate=F)+
  geom_vline(xintercept=c_true,linetype="dashed",col="red",alpha=.5)+
  geom_hline(yintercept=w_true,linetype="dashed",col="red",alpha=.5)+
  scale_fill_viridis_c(name="")+
  coord_fixed(xlim=c(0,1),ylim=c(0,1))+
  labs(x="c",y="w",
       subtitle = TeX(paste0("Spearman's $\\rho=",
                             round(kl_sp["c","w"],digits=3),"$")))+
  ggthemes::theme_few()+
  theme(plot.subtitle = element_text(hjust=0))
  ggthemes::theme_few()

all_plot <-(gamma_c_plot +
              gamma_w_plot+
              c_w_plot)+
  plot_layout(ncol=1,guides = "collect")+
  patchwork::plot_annotation(theme=theme(text=element_text(size=15)))
all_plot
ggsave(all_plot,filename=path(mdir,glue("{ps}.jpeg")),width=4,height=9)
ggsave(all_plot,filename=path(mdir,glue("{ps}.pdf")),width=4,height=9)
