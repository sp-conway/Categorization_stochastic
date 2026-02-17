# NOTE THESE FUNCTIONS ASSUME TWO CATEGORIES NAMED A AND B
# does not work on >2 categories, with more than 2 dimensions
similarity <- function(c, w, stim_1, stim_2, r=1){
  d <- ( (w*abs(stim_1[1]-stim_2[1])^r) + ((1-w)*abs(stim_1[2]-stim_2[2])^r) ) ^(1/r)
  s <- exp(-c*d)
  return(s)
} 
gcm_predict <- function(test, params, r, A_exemplars, B_exemplars){
  n_exemplars <- nrow(A_exemplars)
  stopifnot(nrow(A_exemplars)==nrow(B_exemplars))
  
  # grab params
  c <- ifelse(is.na(params["c"]),1,params["c"])
  b_A <- ifelse(is.na(params["b_A"]), 0.5, params["b_A"])
  gamma <- ifelse(is.na(params["gamma"]),1,params["gamma"])
  w <- ifelse(is.na(params["w"]), 0.5, params["w"])
  
  # sum similarities
  ss_A <- sum(purrr::map_dbl(1:n_exemplars,~similarity(c, w, test, A_exemplars[.x,], r)))
  ss_B <- sum(purrr::map_dbl(1:n_exemplars,~similarity(c, w, test, B_exemplars[.x,], r)))
  p_A <- (ss_A^gamma)*b_A / ( (ss_A^gamma)*b_A + (ss_B^gamma)*(1-b_A) )
  return(unname(p_A))
  # if(return_SS){
  #   return(c("A"=ss_A,"B"=ss_B))
  # }else{
  #   
  # }
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
    # print("=====")
    # print(unname(test[i,]))
    p1[i] <- gcm_predict(test=test[i,],params=params_1,r=r,A_exemplars=A_exemplars,B_exemplars=B_exemplars)
    p0[i] <- gcm_predict(test=test[i,],params=params_0,r=r,A_exemplars=A_exemplars,B_exemplars=B_exemplars)
    # print("p1")
    # print(p1[i])
    # print("p0")
    # print(p0[i])
    kl[i] <- kl_binomial(n=N,p1=p1[i],p0=p0[i])
    # print("kl")
    # print(kl[i])
  }
  if(debug){
    if(any(kl==0)){
      browser()
    }
  }
  # browser()
  kl_all <- exp(sum(log(kl)))
  return(kl_all)
}
