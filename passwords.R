letters <- c('a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l', 'm','n','o','p','q','r','s','t','u','v','w','x','y','z')
letters_and_numbers <- c(letters, 0:9)

count <- 0
n_iters <- 100000

for (i in 1:n_iters)
{
  password_p1 <- sample(letters, 1, replace=T)
  password_p2 <- sample(letters_and_numbers, 4, replace=T)
  
  password <- c(password_p1, password_p2)
  
  #if the password is the same as reversed increase the counter by 1
  if (identical(password, rev(password)))
  {
    count <- count + 1
  }
}
#probability of how many passwords out of the 100000 passwords are the same as reversed
count/n_iters
