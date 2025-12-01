# NOTE THESE FUNCTIONS ASSUME TWO CATEGORIES NAMED A AND B
# does not work on >2 categories, with more than 2 dimensions
similarity <- function(c, w, stim_1, stim_2, r=1){
  d <- ( (w*abs(stim_1[1]-stim_2[1])^r) + ((1-w)*abs(stim_1[2]-stim_2[2])^r) ) ^(1/r)
  s <- exp(-c*d)
  return(s)
} 
gcm_predict <- function(test, params, r, A_exemplars, B_exemplars, return_SS=F){
  n_exemplars <- nrow(A_exemplars)
  stopifnot(nrow(A_exemplars)==nrow(B_exemplars))
  # grab params
  if(is.na(params["c"])){
    c <- 1
  }else{
    c <- params["c"]
  }
  if(is.na(params["b_A"])){
    b_A <- .5
  }else{
    b_A <- params["b_A"]
  }
  if(is.na(params["gamma"])){
    gamma <- 1
  }else{
    gamma <- params["gamma"]
  }
  if(is.na(params["w"])){
    w <- .5
  }else{
    w <- params["w"]
  }
  
  # similarities
  sim_A <- sim_B <- numeric(n_exemplars)
  for(i in 1:n_exemplars){
    sim_A[i] <- similarity(c, w, test, A_exemplars[i,], r)
    sim_B[i] <- similarity(c, w, test, B_exemplars[i,], r)
  }
  # sum similarities
  ss_A <- sum(sim_A)
  ss_B <- sum(sim_B)
  if(return_SS){
    return(c("A"=ss_A,"B"=ss_B))
  }else{
    p_A <- (ss_A^gamma)*b_A / ( (ss_A^gamma)*b_A + (ss_B^gamma)*(1-b_A) )
    return(p_A)
  }
}

gcm_lik <- function(dat, test, params, r, A_exemplars, B_exemplars, do_nllik=T){
  n_stim <- nrow(test)
  lik <- numeric(n_stim)
  for(i in 1:n_stim){
    lik[i] <- dbinom(dat[i,1],sum(dat[i,]),prob=gcm_predict(test[i,],params,r,A_exemplars,B_exemplars))
  }
  if(do_nllik){
    nllik <- -sum(log(lik))
    return(nllik)
  }else{
    return(prod(lik))
  }
}

gcm_kl <- function(N, test, r, A_exemplars, B_exemplars, params_1, params_0,debug=F){
  n_stim <- nrow(test)
  p1 <- p0 <- kl <- numeric(n_stim)
  # browser()
  for(i in 1:n_stim){
    p1[i] <- gcm_predict(test[i,],params_1,r,A_exemplars,B_exemplars)
    p0[i] <- gcm_predict(test[i,],params_0,r,A_exemplars,B_exemplars)
    kl[i] <- kl_binomial(n=N,p1=p1[i],p0=p0[i])
  }
  if(debug){
    if(any(kl==0)){
      browser()
    }
  }
  kl_all <- exp(sum(log(kl)))
  print(kl_all)
  return(kl_all)
}
