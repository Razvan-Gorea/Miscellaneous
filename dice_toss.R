#fair dice tossed 600 times
x <- sample(c(1:6), 600, replace=T)

#estimated probability
ps <-table(x)/600
ps

#probability of getting even number
even <- ps[2] + ps[4] + ps[6]
even

#probability of getting odd number
odd <- ps[1] + ps[3] + ps[5]
odd