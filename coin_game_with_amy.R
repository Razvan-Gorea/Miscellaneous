#Copy and paste the contents of the files into the console to run it
#Comment out certain parts before you in it in console

#Amy receives two euro for a head and losses two euro for a tail 
#She plays the game 100 times
x <- sample(c(-2, 2), 100, replace=T)

run_total <- 0
run_total[1] <- x[1]

for (i in 2:100) run_total[i] = run_total[i - 1] + x[i]
plot(run_total)

#how much she made or loss at the end of the 100 games
sum(x)