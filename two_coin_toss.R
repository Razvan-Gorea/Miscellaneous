#Script to toss two coins at once for 10000 tosses
#Then to find the relative frequency of each outcome
x <- sample(c('HT', 'TH', 'HH', 'TT'), 10000, replace=T)
table(x)/10000