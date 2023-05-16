#Script to pick out heads or tails for 1000 tosses (one fair coin)
#Then to find the probability for getting a head or tail
x <- sample(c('H', 'T'), 1000, replace=T)
table(x)/1000