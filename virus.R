pos <- 0
virus <- 0
for(i in c(1:100000))
{
  if(runif(1) < 0.25)
  {
    virus[i] <- 1
    if(runif(1) < 0.99) pos[i] <- 1 else pos[i] <- 0
  }
  else
  {
    virus[i] <- 0
    if(runif(1) < 0.12) pos[i] <- 1 else pos[i] <- 0
  }
}