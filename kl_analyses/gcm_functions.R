# NOTE THESE FUNCTIONS ASSUME TWO CATEGORIES NAMED A AND B
# does not work on >2 categories, with more than 2 dimensions
distance <- function(stim_1, stim_2) c(abs(stim_1[1]-stim_2[1]),abs(stim_1[2]-stim_2[2]))
similarity <- function(c, w, d, r=1){
  s <- exp(-c* ( (w*d[1]^r) + ((1-w)*d[2]^r) )^(1/r) )
  return(s)
} 
gcm_predict <- function(A_exemplar_dists, B_exemplar_dists, params, r){
  n_exemplars <- nrow(A_exemplar_dists)
  # stopifnot(nrow(A_exemplar_dists)==nrow(B_exemplar_dists))
  
  # grab params
  c <- params[1]#ifelse(is.na(params["c"]),1,params["c"])
  b_A <- .5#ifelse(is.na(params["b_A"]), 0.5, params["b_A"])
  gamma <- params[2]#ifelse(is.na(params["gamma"]),1,params["gamma"])
  w <- params[3]#ifelse(is.na(params["w"]), 0.5, params["w"])
  
  # sum similarities
  ss_A <- sum(purrr::map_dbl(1:n_exemplars,~similarity(c, w, A_exemplar_dists[.x,], r)))
  ss_B <- sum(purrr::map_dbl(1:n_exemplars,~similarity(c, w, B_exemplar_dists[.x,], r)))
  p_A <- (ss_A^gamma)*b_A / ( (ss_A^gamma)*b_A + (ss_B^gamma)*(1-b_A) )
  return(unname(p_A))
  # if(return_SS){
  #   return(c("A"=ss_A,"B"=ss_B))
  # }else{
  #   
  # }
}
# 
# gcm_lik <- function(dat, params, r, A_exemplar, B_exemplar_dists, do_nllik=T){
#   n_stim <- nrow(test)
#   lik <- numeric(n_stim)
#   for(i in 1:n_stim){
#     lik[i] <- dbinom(dat[i,1],sum(dat[i,]),prob=gcm_predict(test[i,],params,r,A_exemplar_dists,B_exemplar_dists))
#   }
#   if(do_nllik){
#     nllik <- -sum(log(lik))
#     return(nllik)
#   }else{
#     return(prod(lik))
#   }
# }

# gcm_kl <- function(N, A_exemplar_dists, B_exemplar_dists, r, params_1, params_0,debug=F){
#   n_stim <- dim(A_exemplar_dists)[1] # NEEDS TO BE THE CASE THAT SAME NUMBER OF EXEMPLAR DISTS FOR A AND B
#   p1 <- p0 <- kl <- numeric(n_stim)
#   # browser()
#   for(i in 1:n_stim){
#     # print("=====")
#     # print(unname(test[i,]))
#     p1[i] <- gcm_predict(A_exemplar_dists=A_exemplar_dists[i,,],B_exemplar_dists=B_exemplar_dists[i,,],params=params_1,r=r)
#     p0[i] <- gcm_predict(A_exemplar_dists=A_exemplar_dists[i,,],B_exemplar_dists=B_exemplar_dists[i,,],params=params_0,r=r)
#     # print("p1")
#     # print(p1[i])
#     # print("p0")
#     # print(p0[i])
#     kl[i] <- kl_binomial(n=N,p1=p1[i],p0=p0[i])
#     # print("kl")
#     # print(kl[i])
#   }
#   if(debug){
#     if(any(kl==0)){
#       browser()
#     }
#   }
#   # browser()
#   kl_all <- exp(sum(log(kl)))
#   return(kl_all)
# }
