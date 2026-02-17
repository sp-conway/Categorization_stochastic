rm(list=ls())
library(tidyverse)
library(here)
library(fs)
avg_area <- 14681.491501619801
f <- here("experiments/turtles_task_switching/data/test/") %>%
  dir_ls()
d <- read_csv(f)
# 
train <- d %>%
  filter(!is.na(key_resp_training.keys)) %>%
  select(participant,condition,stim,category,category_A_label,category_B_label,angle_psy,radius_psy,angle,radius,thisN,
         key_resp_training.keys,key_resp_training.corr,key_resp_training.rt) %>%
  mutate(thisN=thisN+1,
         category_A_label=str_sub(tolower(category_A_label),1,1),
         category_B_label=str_sub(tolower(category_B_label),1,1),
         choice=case_when(
           category_A_label=="f" & key_resp_training.keys=="f"~"A",
           category_A_label=="j" & key_resp_training.keys=="j"~"A",
           category_B_label=="f" & key_resp_training.keys=="f"~"B",
           category_B_label=="j" & key_resp_training.keys=="j"~"B"
         ),
         corr=case_when(
           choice=="A" & category=="A"~1,
           choice=="A" & category=="B"~0,
           choice=="B" & category=="B"~1,
           choice=="B" & category=="A"~0,
         ))
train$corr==train$key_resp_training.corr


size_train <- d %>%
  filter(!is.na(key_resp_size_judgment.keys)) %>%
  select(participant,condition,stim,category,angle_psy,radius_psy,angle,radius,thisN,area,
         key_resp_size_judgment.keys,
         key_resp_size_judgment.corr,
         key_resp_size_judgment.rt) %>%
  mutate(choice=case_when(
    key_resp_size_judgment.keys=="f"~"smaller",
    key_resp_size_judgment.keys=="j"~"larger",
  ))

check <- size_train %>%
  mutate(check=case_when(
    area < avg_area & key_resp_size_judgment.keys=="f"~1,
    area < avg_area & key_resp_size_judgment.keys=="j"~0,
    area > avg_area & key_resp_size_judgment.keys=="f"~0,
    area > avg_area & key_resp_size_judgment.keys=="j"~1
  ))
check$check==check$key_resp_size_judgment.corr

transfer_standard <- d %>%
  filter(!is.na(key_resp_transfer_standard.keys)) %>%
  filter(!is.na(key_resp_transfer_standard.keys)) %>%
  select(participant,condition,stim,category,angle_psy,radius_psy,angle,radius,thisN,trial_type,
         key_resp_transfer_standard.keys,
         key_resp_transfer_standard.rt)
prop.table(table(transfer_standard$trial_type))

transfer_switch <- d %>%
  filter(!is.na(key_resp_transfer_switch.keys)) %>%
  filter(!is.na(key_resp_transfer_switch.keys)) %>%
  select(participant,condition,stim,category,angle_psy,radius_psy,angle,radius,thisN,trial_type,
         key_resp_transfer_switch.keys,
         key_resp_transfer_switch.rt)
prop.table(table(transfer_switch$trial_type) )

t=tibble(t=transfer_standard$trial_type)

X=0
for(i in 2:nrow(t)){
  if(t$t[i]=="switch"){
    if(t$t[i-1]=="switch"){
      X=X+1
    }
  }
}
X
