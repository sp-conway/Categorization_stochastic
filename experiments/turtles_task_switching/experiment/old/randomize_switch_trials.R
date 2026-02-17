rm(list=ls())
library(here)
library(tidyverse)
s <- here("experiments/turtles_task_switching/stim/stim_transfer_switch.csv") %>%
  read_csv()
standard <- s %>%
  filter(trial_type=="standard") %>%
  mutate(n=1:n())
switch <- s %>%
  filter(trial_type=="switch") %>%
  mutate(n=1:n())
randomize_trials <- function(n_standard=40,n_switch=15, switch, standard){
  do_random <- T
  unshuffled <- c(rep(0,n_standard-1),rep(1,n_switch))
  n_total <- length(unshuffled)
  st <- Sys.time()
  while (do_random) {
    shuffled_tmp <- c(0,sample(unshuffled,n_total,replace=F))
    shuffled_tmp_cumsum <- cumsum(shuffled_tmp) 
    check <- logical(n_total-2)
    for(i in 3:n_total){
      check[i] <- (shuffled_tmp_cumsum[i]>shuffled_tmp_cumsum[i-1]) & (shuffled_tmp_cumsum[i-1]>shuffled_tmp_cumsum[i-2])
    }
    if(sum(check)==0) do_random <- F
  }
  n_total <- n_total+1
  end <- Sys.time()
  time <- end-st
  print(time)
  shuffled <- shuffled_tmp
  print(shuffled)
  reg <- which(shuffled==0)
  sw <- which(shuffled==1)
  standard_indices_shuffled <- sample(standard$n, nrow(standard), replace = F)
  switch_indices_shuffled <- sample(switch$n, nrow(switch), replace = F)
  
  trials_shuffled <- tibble(
    stim=numeric(),
    category=character(),
    angle_psy=numeric(),
    radius_psy=numeric(),
    angle=numeric(),
    radius=numeric(),
    trial_type=character(),
    area=numeric()
  )
  standard_current_index <- switch_current_index <- 1
  for(i in 1:n_total){
    if(shuffled[i]==0){
      trials_shuffled <- bind_rows(trials_shuffled,
                                   standard %>% filter(n==standard_indices_shuffled[standard_current_index]))
      standard_current_index <- standard_current_index+1
    }else if(shuffled[i]==1){
      trials_shuffled <- bind_rows(trials_shuffled,
                                   switch %>% filter(n==switch_indices_shuffled[switch_current_index]))
      switch_current_index <- switch_current_index+1
    }
  }
  
  # print(time)
  trials_shuffled <- trials_shuffled %>%
    select(-n) %>%
    mutate(trial_n=1:n()) %>%
    relocate(trial_n,.before=everything())
  return(trials_shuffled)
  # return(time)
}

n_sim <- 10000
do_sim <- F
if(do_sim){
  time <- numeric(n_sim)
  for(i in 1:n_sim){
    print(i)
    time[i] <- randomize_trials()
  }
  par(mfrow=c(1,1))
  hist(time)
  summary(time)
}

tmp <- randomize_trials(standard=standard,switch=switch) 

