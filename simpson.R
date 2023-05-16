#Import simpsons_episode.csv
#run attach(simpsons_episodes) in console
#Copy code and run in console

#Q1
mean(imdb_rating, na.rm = TRUE)

#Q2
sd(imdb_rating, na.rm = TRUE)

#Q3
hist(imdb_rating)

#Q4
my_vect = c()
my_vect2 = c()
for (x in 1:600){
  if (season[x] <= 10 && season[x] >= 1){
    my_vect <- c(my_vect, imdb_rating[x])
  }else if (season[x] <= 20 && season[x] >= 10){
    my_vect2 <- c(my_vect2, imdb_rating[x])
  }
}

hist(my_vect, breaks = 5)
hist(my_vect2, breaks = 5)

#Q5
hist(my_vect, breaks = 10)
hist(my_vect2, breaks = 10)

#Q6
boxplot(imdb_rating, ylab='rating')

#Q7
my_vect3 = c()
for (x in 1:600){
  if (season[x] == 10){
    my_vect3 <- c(my_vect3, imdb_rating[x])
  }
}
boxplot(my_vect3, ylim = c(6.5,8.5))

#Q8
ratings1 = c()
ratings2 = c()
ratings3 = c()
ratings4 = c()
ratings5 = c()
ratings6 = c()
ratings7 = c()
ratings8 = c()
ratings9 = c()
ratings10 = c()
ratings11 = c()
ratings12 = c()
ratings13 = c()
ratings14 = c()
ratings15 = c()
ratings16 = c()
ratings17 = c()
ratings18 = c()
ratings19 = c()
ratings20 = c()
ratings21 = c()
ratings22 = c()
ratings23 = c()
ratings24 = c()
ratings25 = c()
ratings26 = c()
ratings27 = c()
ratings28 = c()
 
for (x in 1:600)
{
    if (season[x] == 1)
    {
      ratings1 <- c(ratings1, imdb_rating[x])
    }else if (season[x] == 2)
    {
      ratings2 <- c(ratings2, imdb_rating[x])
    }else if (season[x] == 3)
    {
      ratings3 <- c(ratings3, imdb_rating[x])
    }else if (season[x] == 4)
    {
      ratings4 <- c(ratings4, imdb_rating[x])
    }else if (season[x] == 5)
    {
      ratings5 <- c(ratings5, imdb_rating[x])
    }else if (season[x] == 6)
    {
      ratings6 <- c(ratings6, imdb_rating[x])
    }else if (season[x] == 7)
    {
      ratings7 <- c(ratings7, imdb_rating[x])
    }else if (season[x] == 8)
    {
      ratings8 <- c(ratings8, imdb_rating[x])
    }else if (season[x] == 9)
    {
      ratings9 <- c(ratings9, imdb_rating[x])
    }else if (season[x] == 10)
    {
      ratings10 <- c(ratings10, imdb_rating[x])
    }else if (season[x] == 11)
    {
      ratings11 <- c(ratings11, imdb_rating[x])
    }else if (season[x] == 12)
    {
      ratings12 <- c(ratings12, imdb_rating[x])
    }else if (season[x] == 13)
    {
      ratings13 <- c(ratings13, imdb_rating[x])
    }else if (season[x] == 14)
    {
      ratings14 <- c(ratings14, imdb_rating[x])
    }else if (season[x] == 15)
    {
      ratings15 <- c(ratings15, imdb_rating[x])
    }else if (season[x] == 16)
    {
      ratings16 <- c(ratings16, imdb_rating[x])
    }else if (season[x] == 17)
    {
      ratings17 <- c(ratings17, imdb_rating[x])
    }else if (season[x] == 18)
    {
      ratings18 <- c(ratings18, imdb_rating[x])
    }else if (season[x] == 19)
    {
      ratings19 <- c(ratings19, imdb_rating[x])
    }else if (season[x] == 20)
    {
      ratings20 <- c(ratings20, imdb_rating[x])
    }else if (season[x] == 21)
    {
      ratings21 <- c(ratings21, imdb_rating[x])
    }else if (season[x] == 22)
    {
      ratings22 <- c(ratings22, imdb_rating[x])
    }else if (season[x] == 23)
    {
      ratings23 <- c(ratings23, imdb_rating[x])
    }else if (season[x] == 24)
    {
      ratings24 <- c(ratings24, imdb_rating[x])
    }else if (season[x] == 25)
    {
      ratings25 <- c(ratings25, imdb_rating[x])
    }else if (season[x] == 26)
    {
      ratings26 <- c(ratings26, imdb_rating[x])
    }else if (season[x] == 27)
    {
      ratings27 <- c(ratings27, imdb_rating[x])
    }else if (season[x] == 28)
    {
      ratings28 <- c(ratings28, imdb_rating[x])
    }
}

holder = c()
holder <- c(holder, mean(ratings1), mean(ratings2), mean(ratings3), mean(ratings4), mean(ratings5), mean(ratings6), mean(ratings7), mean(ratings8), mean(ratings9), mean(ratings10), mean(ratings11), mean(ratings12), mean(ratings13), mean(ratings14), mean(ratings15), mean(ratings16), mean(ratings17), mean(ratings18), mean(ratings19), mean(ratings20), mean(ratings21), mean(ratings22), mean(ratings23), mean(ratings24), mean(ratings25), mean(ratings26), mean(ratings27), mean(ratings28))
plot(holder, xlab = 'Seasons', ylab = 'Rating', main = 'IMDB AVERAGE RATING PER SEASON OF THE SIMPSONS')
