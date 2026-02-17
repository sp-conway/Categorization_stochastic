# setting up stimuli for categorization task switching experiment 
rm(list=ls())
library(here)
library(patchwork)
library(tidyverse)


# Read in mds solution, raw stimulus values for each stimulus ====================================
mds <- here("mds_turtles/mds_turtles.csv") %>%
  read_csv()
orig <- here("mds_turtles/orig_turtles.csv") %>%
  read_csv()

# gcm functions
source(here("experiments/turtles_task_switching/experiment/gcm_functions.R"))

# plot stimuli ========================================================================
p_mds <- mds %>%
  ggplot(aes(angle,radius))+
  geom_text(aes(label=stim))+
  geom_abline(slope=1,intercept=0,linetype="dashed",alpha=.4)+
  labs(title="MDS")+
  coord_fixed(xlim=c(-50,50),ylim=c(-50,50))+
  ggthemes::theme_few()+
  theme(plot.title=element_text(hjust=0.5))
p_orig <- orig %>%
  ggplot(aes(angle,radius))+
  geom_text(aes(label=stim))+
  geom_abline(slope=-1,intercept=0,linetype="dashed",alpha=.4)+
  labs(title="Physical")+
  # coord_fixed(xlim=c(-50,50),ylim=c(-50,50))+
  ggthemes::theme_few()+
  theme(plot.title=element_text(hjust=0.5))
p_orig|p_mds

# determine categories ===============================================================
# stimuli near the diagonal are "test" stimuli - untrained
mds_cat <- mds %>%
  mutate(category=case_when(
    stim %in% c(1,7,13,19,25)~"Test",
    radius>angle ~ "A",
    angle>radius ~ "B"
  ))

# function that plots categories and saves file
plot_categories <- function(mds_cat, path){
  p_mds_cat <-  mds_cat %>%
    ggplot(aes(angle,radius,col=category))+
    geom_text(aes(label=stim),show.legend=F)+
    geom_point(alpha=0)+
    geom_abline(slope=1,intercept=0,linetype="dashed",alpha=.4)+
    ggsci::scale_color_futurama()+
    # labs(title="MDS")+
    coord_fixed(xlim=c(-50,50),ylim=c(-50,50))+
    ggthemes::theme_few()+
    theme(plot.title=element_text(hjust=0.5),
          legend.position="right",
          text=element_text(size=14))+
    guides(colour=guide_legend(override.aes=list(alpha=1)))
  ggsave(filename=path, width=4,height=4)
  return(p_mds_cat)
}

p_mds_cat <- plot_categories(mds_cat,here("experiments/turtles_task_switching/experiment/plots/category_stim_plot.jpeg"))
p_mds_cat 

# testing gcm predictions =================================================

# A exemplars
A_exemplars <- mds_cat %>%
  filter(category=="A") %>%
  select(angle,radius) %>%
  as.matrix()

# B exemplars
B_exemplars <- mds_cat %>%
  filter(category=="B") %>%
  select(angle,radius) %>%
  as.matrix()

# test stimuli
test_stim <- mds_cat %>%
  filter(category=="Test") %>%
  select(angle,radius,stim) %>%
  as.matrix()

n_test <- nrow(test_stim)
p <- matrix(NA, nrow=n_test, ncol=1)
rownames(p) <- test_stim[,3]
test_stim <- test_stim[,1:2]

# setup reasonable parameters
c <- .1
gamma <- 1
b_A <- .5
r <- 1
w <- .5

params <- c("c"=c,
            "w"=w,
            "b_A"=b_A,
            "gamma"=gamma)
# gcm probabilities
for(i in 1:n_test){
  p[i,] <- gcm_predict(test_stim[i,], params, r, A_exemplars, B_exemplars)
}
p
# gcm sum similarities
for(i in 1:n_test){
  print(gcm_predict(test_stim[i,], params, r, A_exemplars, B_exemplars, return_SS=T))
}

# set up training, transfer stimuli =========================================================================
# need to join to physical stimulus values
mds_cat_with_orig <- mds_cat %>% 
  rename(angle_psy=angle,
         radius_psy=radius) %>%
  left_join(orig) %>%
  relocate(c(stim, category), .before=everything())

# training stimuli - just everything but the ambiguous test stimuli
train <- mds_cat_with_orig %>%
  filter(category!="Test") 

# IMPORTANT - for ambiguous test stimuli, need to repeat them more. 
# more trials for unlearned stimuli
n_test_repeats <- 4

# TRANSFER TRIALS W/O SWITCH
transfer <- mds_cat_with_orig %>%
  filter(category=="Test") %>%
  slice(rep(1:n(),n_test_repeats)) %>%
  bind_rows(train) %>%
  mutate(trial_type="standard")

# IMPORTANT - ADD IN "SWITCH" STIMULI
# will ask people about test stimuli, plus a handful of other selected stimuli
switch_stim <- mds_cat_with_orig %>%
  filter(category=="Test" | stim %in% c(2,5,15,20,6,24,17,21,16,10)) 

# IMPORTANT MATCHING LENGTH OF TRANSFER STANDARD TO TRANSFER SWITCH
# basically will just have the 15 switch trials but they are regular trials
transfer_with_switch <- transfer %>%
  bind_rows(mutate(switch_stim,trial_type="switch")) 

transfer_standard <- transfer %>%
  bind_rows(mutate(switch_stim,trial_type="switch")) 

table(transfer_with_switch$trial_type)
table(transfer_standard$trial_type)
table(transfer_with_switch$category,transfer_with_switch$trial_type)

# figure out areas =========================================================================================
wedge_radius <- 150 # fixed in the experiment.

get_turtle_area <- function(shell_radius,wedge_angle,wedge_radius=150){
  shell_angle <- 180-wedge_angle
  shell_area <- (pi*shell_radius^2)*(shell_angle/360)
  wedge_area <- (pi*wedge_radius^2)*(wedge_angle/360)
  turtle_area <- shell_area+wedge_area
  return(turtle_area)
}

# Training stimuli - need to get areas here
# because there is a size judgment training block
orig_train_only <- orig %>% # IMPORTANT ONLY INCLUDE AVERAGE TRAINING STIMULI
  filter(stim %in% train$stim) %>%
  mutate(area=get_turtle_area(radius,angle))

# Finding areas for all stimuli
orig_all_with_areas <- orig %>%
  mutate(area=get_turtle_area(radius,angle))

# Transfer stimuli - add in areas
transfer_with_switch_areas_included <- transfer_with_switch %>%
  mutate(area=get_turtle_area(radius,angle))

# Figure out "average" turtle size
avg_turtle_phy <- tibble(
  radius=mean(orig_train_only$radius),
  angle=mean(orig_train_only$angle),
  area=get_turtle_area(radius,angle)
)

# Plot histograms of training stimuli area, want to make sure average turtle is actually central tendency
par(mfrow=c(1,3))
hist(orig_train_only$radius,main="radius")
abline(v=avg_turtle_phy$radius,col='red')
hist(orig_train_only$angle,main="angle")
abline(v=avg_turtle_phy$angle,col='red')
hist(orig_train_only$area,main="area")
abline(v=avg_turtle_phy$area,col='red')

# whether you consider all turtles from training or across the whole experiment,
# the average turtle's area is similar to the average of all turtles
avg_turtle_phy
mean(orig_all_with_areas$area)
median(orig_all_with_areas$area)
mean(orig_train_only$area)
median(orig_train_only$area)

# write stim to file ============================================================
write_csv(mds_cat_with_orig, file=here("experiments/turtles_task_switching/experiment/stim/stim_all.csv"))

transfer_with_switch_areas_included %>%
  write_csv(here("experiments/turtles_task_switching/experiment/stim/stim_transfer_switch.csv"))

# transfer stimuli - no areas
transfer_standard %>%
  write_csv(here("experiments/turtles_task_switching/experiment/stim/stim_transfer_standard.csv"))

# train stimuli - no areas
train %>%
  write_csv(here("experiments/turtles_task_switching/experiment/stim/stim_train.csv"))

# train stimuli - no areas
orig_train_only %>%
  left_join(train) %>% # getcategory label, psy values too
  relocate(category,angle_psy,radius_psy,.after=stim) %>%
  write_csv(here("experiments/turtles_task_switching/experiment/stim/stim_train_with_areas.csv"))

# average turtle
avg_turtle_phy %>%
  left_join(
    orig
  ) %>%
 left_join(mds %>% rename(angle_psy=angle,radius_psy=radius)) %>%
  relocate(stim,.before=everything()) %>%
  write_csv(here("experiments/turtles_task_switching/experiment/stim/stim_avg_turtle.csv"))

  
