rm(list=ls())
library(here)
library(tidyverse)
library(fs)

d <- here("experiments/turtles_task_switching/data/clean/category_training.csv") %>%
  read_csv()

# prop correct overall ========================================================================================
prop_correct_overall_by_ppt <- d %>%
  group_by(participant) %>%
  summarise(p=mean(correct)) %>%
  ungroup()
ggplot(prop_correct_overall_by_ppt,aes(p))+
  geom_histogram(fill="lightblue")+
  geom_vline(xintercept=.5)+
  ggthemes::theme_few()

# prop correct last block ========================================================================================
prop_correct_last_block_by_ppt <- d %>%
  filter(block_n==max(block_n)) %>%
  group_by(participant) %>%
  summarise(p=mean(correct)) %>%
  ungroup()
ggplot(prop_correct_last_block_by_ppt,aes(p))+
  geom_histogram(fill="lightblue")+
  geom_vline(xintercept=.5)+
  ggthemes::theme_few()

# check to make sure f/j label didn't matter  ========================================================================================
prop_correct_overall_by_ppt_label <- d %>%
  group_by(participant) %>%
  summarise(p=mean(correct)) %>%
  ungroup() %>%
  left_join(distinct(d,participant,category_A_label)) 
ggplot(prop_correct_overall_by_ppt_label,aes(p))+
  geom_histogram(fill="lightblue")+
  geom_vline(xintercept=.5)+
  facet_grid(category_A_label~.)+
  ggthemes::theme_few()
