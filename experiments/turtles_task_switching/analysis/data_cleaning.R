# CLEANING AND CHECKING DATA FROM TURTLES TASK SWITCHING EXPERIMENT

# SETUP ==========================================================================================
rm(list=ls())
library(tidyverse)
library(here)
library(glue)
library(fs)

# all raw csv files
f_all <- here("experiments/turtles_task_switching/data/raw/") %>%
  dir_ls(regexp = ".csv")

# IMPORT ALL RAW DATA FILES ======================================================================
read <- function(f){
  f %>%
    read_csv() %>% # because R reads "f" as FALSE and there are too many columns to specify all types
    mutate(category_A_label=tolower(str_sub(as.character(category_A_label),
                                    1,1)),
           category_B_label=tolower(str_sub(as.character(category_B_label),
                                            1,1)))
}
d_all <- map(f_all,read) %>%
  list_rbind()

# CLEAN AND CHECK CATEGORY TRAINING DATA ======================================================================
category_train <- d_all %>%
  filter(!is.na(key_resp_training.keys)) %>%
  select(participant,stim,
         condition,
         category_A_label,
         category_B_label,
         category,angle,
         radius,
         angle_psy,
         radius_psy,
         key_resp_training.keys,
         key_resp_training.corr,
         key_resp_training.rt,
         training.thisRepN,
         thisN) %>%
  rename(rt=key_resp_training.rt,
         correct=key_resp_training.corr,
         key_choice=key_resp_training.keys) %>%
  mutate(block_n=training.thisRepN+1, # python is 0 indexed, R is 1 indexed
         trial_n=thisN+1,
         category_choice=case_when(
           category_A_label=="f" & key_choice=="f"~"A",
           category_A_label=="j" & key_choice=="j"~"A",
           category_B_label=="f" & key_choice=="f"~"B",
           category_B_label=="j" & key_choice=="j"~"B",
           T~NA_character_
         )) %>%
  select(-c(training.thisRepN,thisN))

# check that participant's accuracy was recorded correctly 
check_category_train_correct <- function(category_train){
  check <- category_train %>%
    mutate(correct1=case_when(
      category_choice=="A" & category=="A"~1,
      category_choice=="A" & category=="B"~0,
      category_choice=="B" & category=="A"~0,
      category_choice=="B" & category=="B"~1,
      T~NA
    ))
  if(all(check$correct==check$correct1)){
    print("Check Passed")
  }else{
    stop("Check Failed")
  }
}
check_category_train_correct(category_train)

# write cleaned data to file
write_csv(category_train,file=here("experiments/turtles_task_switching/data/clean/category_training.csv"))

# SIZE JUDGMENT TRAINING ==========================================================================================
size_train <- d_all %>%
  filter(!is.na(key_resp_size_judgment.keys)) %>%
  select(participant,stim,
         condition,
         area,
         angle,
         radius,
         angle_psy,
         radius_psy,
         key_resp_size_judgment.keys,
         key_resp_size_judgment.corr,
         key_resp_size_judgment.rt,
         size_judgment_trials.thisRepN,
         thisN) %>%
  rename(rt=key_resp_size_judgment.rt,
         correct=key_resp_size_judgment.corr,
         key_choice=key_resp_size_judgment.keys) %>%
  mutate(block_n=size_judgment_trials.thisRepN+1, # python is 0 indexed, R is 1 indexed
         trial_n=thisN+1,
         choice=case_match(key_choice,
                           "f"~"smaller",
                           "j"~"larger")) %>%
  select(-c(size_judgment_trials.thisRepN,thisN))

check_size_train_correct <- function(size_train){
  avg_area <- here("experiments/turtles_task_switching/experiment/stim/stim_avg_turtle.csv") %>%
    read_csv(progress = F) %>%
    pull(area)
  check <- size_train %>%
    mutate(correct1=case_when(
      area<avg_area & choice=="smaller"~1,
      area>avg_area & choice=="smaller"~0,
      area<avg_area & choice=="larger"~0,
      area>avg_area & choice=="larger"~1,
      T~NA
    ))
  if(all(check$correct==check$correct1)){
    print("Check Passed")
  }else{
    stop("Check Failed")
  }
}
check_size_train_correct(size_train)

# write to file
write_csv(size_train,file=here("experiments/turtles_task_switching/data/clean/size_judgment_training.csv"))

# TRANSFER STANDARD BLOCK ===========================================================================================
transfer_standard <- d_all %>%
  filter(!is.na(key_resp_transfer_standard.keys)) %>%
  select(participant,
         stim,
         condition,
         category_A_label,
         category_B_label,
         category,angle,
         radius,
         angle_psy,
         radius_psy,
         key_resp_transfer_standard.keys,
         key_resp_transfer_standard.rt,
         trial_type,
         transfer_standard_loop.thisRepN,
         transfer_standard.thisN) %>%
  rename(rt=key_resp_transfer_standard.rt,
         key_choice=key_resp_transfer_standard.keys) %>%
  mutate(block_n=transfer_standard_loop.thisRepN+1, # python is 0 indexed, R is 1 indexed
         trial_n=transfer_standard.thisN+1,
         category_choice=case_when(
           category_A_label=="f" & key_choice=="f"~"A",
           category_A_label=="j" & key_choice=="j"~"A",
           category_B_label=="f" & key_choice=="f"~"B",
           category_B_label=="j" & key_choice=="j"~"B",
           T~NA_character_
         )) %>%
  select(-c(transfer_standard_loop.thisRepN,transfer_standard.thisN))

# double checking that there were no back to back switches
check_transfer_standard_order <- function(transfer_standard){
  ppt_n <- unique(transfer_standard$participant)
  n_p <- length(ppt_n)
  X <- rep(0,n_p)
  for(p in 1:n_p){
    print(p)
    d_tmp <- transfer_standard %>%
      filter(participant==ppt_n[p]) %>%
      arrange(block_n,trial_n)
    if(d_tmp$trial_type[1]=="switch") X[p] <- X[p]+1
    for(i in 2:(nrow(d_tmp)-1)){
      if(d_tmp$trial_type[i]=="switch"){
        if(d_tmp$trial_type[i+1]=="switch"){
          X[p] <- X[p]+1
        }
      }
    }
  }
  if(all(X==0)){
    print("Check Passed")
  }else{
    print("Check Failed")
    print(paste0("Check participants", ppt_n[which(X!=0)]))
  }
}
check_transfer_standard_order(transfer_standard)

# write to file
write_csv(transfer_standard,file=here("experiments/turtles_task_switching/data/clean/transfer_standard.csv"))

# TRANSFER SWITCH BLOCK ===========================================================================================
transfer_switch <- d_all %>%
  filter(!is.na(key_resp_transfer_switch.keys)) %>%
  select(participant,
         stim,
         condition,
         category_A_label,
         category_B_label,
         category,angle,
         radius,
         angle_psy,
         radius_psy,
         key_resp_transfer_switch.keys,
         key_resp_transfer_switch.rt,
         trial_type,
         transfer_switch_loop.thisRepN,
         transfer_switch.thisN) %>%
  rename(rt=key_resp_transfer_switch.rt,
         key_choice=key_resp_transfer_switch.keys) %>%
  mutate(block_n=transfer_switch_loop.thisRepN+1, # python is 0 indexed, R is 1 indexed
         trial_n=transfer_switch.thisN+1,
         category_choice=case_when(
           category_A_label=="f" & key_choice=="f"~"A",
           category_A_label=="j" & key_choice=="j"~"A",
           category_B_label=="f" & key_choice=="f"~"B",
           category_B_label=="j" & key_choice=="j"~"B",
           T~NA_character_
         )) %>%
  select(-c(transfer_switch_loop.thisRepN,transfer_switch.thisN))

# double checking that there were no back to back switches
check_transfer_switch_order <- function(transfer_switch){
  ppt_n <- unique(transfer_switch$participant)
  n_p <- length(ppt_n)
  X <- rep(0,n_p)
  for(p in 1:n_p){
    print(p)
    d_tmp <- transfer_switch %>%
      filter(participant==ppt_n[p]) %>%
      arrange(block_n,trial_n)
    if(d_tmp$trial_type[1]=="switch") X[p] <- X[p]+1
    for(i in 2:(nrow(d_tmp)-1)){
      if(d_tmp$trial_type[i]=="switch"){
        if(d_tmp$trial_type[i+1]=="switch"){
          X[p] <- X[p]+1
        }
      }
    }
  }
  if(all(X==0)){
    print("Check Passed")
  }else{
    print("Check Failed")
    print(paste0("Check participants", ppt_n[which(X!=0)]))
  }
}
check_transfer_switch_order(transfer_switch)

# write to file
write_csv(transfer_switch,file=here("experiments/turtles_task_switching/data/clean/transfer_switch.csv"))

