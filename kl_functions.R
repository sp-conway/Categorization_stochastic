
beta_correction_binomial <- function(n,p1,p0){
  if(any(c(p1,p0)==0)){
    corr <- 0
  }else if(p1==p0){
    corr <- 0
  }else{
    x <- -n * ( (p1*(1-p1))/(p0*(1-p0)) ) * log( sqrt((p1*(1-p1)) ) / sqrt((p0*(1-p0))) )
    y <- ( (p1*(1-p1))^2 - (p0*(1-p0))^2 ) / ( ( ( (2*p0)*(1-p0) )^2)/n)
    corr <- 0#x+y
  }
  return(corr)
}

# kl_binomial <- function(n,p1,p0){ # sampling distribution
#   x <- (p0*(p0/p1))
#   y <- (1-p0)*log((1-p0)/(1-p1))
#   kl <- exp(-n*(x+y)-beta_correction_binomial(n,p1,p0))
#   return(kl)
# }


kl_binomial <- function(n,p1,p0){ # sampling distribution
  # with added code to try and prevent underflow
  xmin <- log(.Machine$double.xmin)
  xmax <- log(.Machine$double.xmax)
  
  #
  if(p0==0){
    p0 <- .Machine$double.xmin
  }else if(p0==1){
    p0 <- .9999999
  }
  if(p1==0){
    p1 <- .Machine$double.xmin
  }else if(p1==1){
    p1 <- .9999999
  }
  x <- p0*log(p0/p1)
  y <- (1-p0)*log((1-p0)/(1-p1))
  z <- -n*(x+y)-beta_correction_binomial(n,p1,p0)
  # if(is.nan(z)){ # temporary bug fix
  #   kl <- 0
  # }else{
  if(z < log(.Machine$double.xmin)){
      kl <- 0
    }else{
      kl <- exp(z)
  }
  
  # print("========")
  # print(p1)
  # print(p0)
  # print(n)
  # print(x)
  # print(y)
  # print(z)
  # print(xmin)
  
  return(kl)
}


