# function takes input params_0 (true parameters) and candidate parameter set params_0,
# in addition to a matrix of stimuli stim, A_exemplar_dists, B_exemplar_dists, distance metric r
# returns numerical sampling distribution kl_pdf
# note that params_0 and params_1 have to be ordered [c,gamma_1,gamma_2,w]
gcm_kl_binomial_split <- function(params_0,params_1,A_exemplar_dists,B_exemplar_dists,r=1){ # sampling distribution
  # number of stimuli in experiment 
  n_stim <- dim(A_exemplar_dists)[1] # NOTE REQUIRES SAME N EXEMPLAR DISTS FOR A AND B
  
  # Do Computations twice, once for gamma 1 and once for gamma 2
  
  # GAMMA 1 =========================================================================
  # gamma 1
  # probabilities under the GCM for c, w, gamma 1
  p0_1 <- purrr::map_dbl(1:n_stim,
                ~gcm_predict(A_exemplar_dists=A_exemplar_dists[.x,,],
                             B_exemplar_dists=B_exemplar_dists[.x,,],
                             params=c(params_0[1],
                               params_0[2],
                               params_0[4]),
                             r=r))
  p1_1 <- purrr::map_dbl(1:n_stim,
                         ~gcm_predict(A_exemplar_dists=A_exemplar_dists[.x,,],
                                      B_exemplar_dists=B_exemplar_dists[.x,,],
                                      params=c(params_1[1],
                                               params_1[2],
                                               params_1[4]),
                                      r=r))
  
  # Gamma 2 ========================================================================
  # probabilities under the GCM for c, w, gamma 2
  p0_2 <- purrr::map_dbl(1:n_stim,
                         ~gcm_predict(A_exemplar_dists=A_exemplar_dists[.x,,],
                                      B_exemplar_dists=B_exemplar_dists[.x,,],
                                      params=c(params_0[1],
                                               params_0[3],
                                               params_0[4]),
                                      r=r))
  p1_2 <- purrr::map_dbl(1:n_stim,
                         ~gcm_predict(A_exemplar_dists=A_exemplar_dists[.x,,],
                                      B_exemplar_dists=B_exemplar_dists[.x,,],
                                      params=c(params_1[1],
                                               params_1[3],
                                               params_1[4]),
                                      r=r))
  
  # KL surface values
  do_kl <- function(p0,p1){
    kl_vec <- p0*log(p0/p1) + (1-p0)*log((1-p0)/(1-p1))
    kl_exp <- exp(-1*kl_vec) # -1 because trial n = 1
    return(kl_exp)
  }
  
  # KL surface value 1
  kl_exp_1 <- do_kl(p0_1,p1_1)
  
  # KL Surface value 2
  kl_exp_2 <- do_kl(p0_2,p1_2)
  
  # KL Correction for sampl dist
  kl_correction <- function(p0,p1){
    sig_0 <- p0*(1-p0)
    sig_1 <- p1*(1-p1)
    sig_fun_1_v <- (sqrt(sig_1)/sqrt(sig_0))^(-1*(sig_1/sig_0))
    sig_fun_2_v <- exp( (sig_1^2 - sig_0^2)/((4*sig_0^2)) )
    correction <- sig_fun_1_v*sig_fun_2_v
    
    # As the variance [sig] gets extreme, the numerical computation of the correction
    # becomes unstable. Also, the effect of the correction here is minimal. 
    # This code reduces the effect of the correction for high sigma
    find_ind1 <- function(x) abs(.5-x)>=.4
    ind <- find_ind1(p0) | find_ind1(p1)
    correction[ind] <- ((sig_fun_1_v[ind]*sig_fun_2_v[ind])+1)/2
    
    # This code eliminates the correction for extreme Sigma
    find_ind2 <- function(x) abs(.5-x)>=.49
    ind <- find_ind2(p0)|find_ind2(p1)
    correction[ind] <- 1
  }
  
  
  # KL CORRECTED VAL. FOR GAMMA 1
  kl_correction_1 <- kl_correction(p0_1,p1_1)
  kl_corrected_1 <- kl_exp_1/kl_correction_1
  
  # KL CORRECTED VAL. FOR GAMMA 2
  kl_correction_2 <- kl_correction(p0_2,p1_2)
  kl_corrected_2 <- kl_exp_2/kl_correction_2
  
  # Compute Final Corrected exp(KL) value as product across trials.
  kl_exp_adj <- prod(kl_corrected_1)*prod(kl_corrected_2)
  return(kl_exp_adj)
}

# this function loops through all parameters 1 to get kl-sampling distribution
# params_0 is vector of true parameters in order [c,gamma_1,gamma_2,w]
# params_min - minimum values for c, gamma_1, gamma_2, w
# params_max - maximum values for c, gamma_1, gamma_2, w
# grain - number of increments per parameter (granularity)
# NOTE: n = 1 implicitly for each trial. 
# increasing n will cause the kl_pdf to approach 0, so need to repeat stimuli if want to include multiple trials of any given stimulus
# A_exemplar_dists - matrix of exemplars for category A
# B_exemplar_dists - matrix of exemplars for category B
gcm_kl_binomial_split_looper <- function(params_0,params_min,params_max,grain,A_exemplar_dists,B_exemplar_dists,r){
  # vectors of all parameters
  c_all <- seq(params_min[1], params_max[1], length.out=grain)
  gamma_1_all <- seq(params_min[2], params_max[2], length.out=grain)
  gamma_2_all <- seq(params_min[3], params_max[3], length.out=grain)
  w_all <- seq(params_min[4], params_max[4], length.out=grain)
  
  # LOOP THROUGH
  kl_exp_adj <- array(NA_real_,dim=rep(grain,4))
  # i <- 1
  N <- grain^4
  for(c in 1:grain){
    cat(c,"/",grain,"\n")
    # st <- Sys.time()
    for(g1 in 1:grain){
      for(g2 in 1:grain){
        for(w in 1:grain){
          kl_exp_adj[c,g1,g2,w] <- gcm_kl_binomial_split(params_0=params_0,
                                                        params_1=c(c_all[c],
                                                          gamma_1_all[g1],
                                                          gamma_2_all[g2],
                                                          w_all[w]),
                                                        A_exemplar_dists=A_exemplar_dists,
                                                        B_exemplar_dists=B_exemplar_dists,
                                                        r)
          # if(!is.finite(kl_exp_adj[c,g1,g2,w])) browser()
          # i <- i+1
        }
      }
    }
    # end <- Sys.time()
    # print(end-st)
  }
  # browser()
  kl_pdf <- kl_exp_adj/sum(kl_exp_adj,na.rm=T)
  return(kl_pdf)
}


