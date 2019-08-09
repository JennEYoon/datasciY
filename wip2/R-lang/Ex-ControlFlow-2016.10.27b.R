#  Title: Example - RIA book p.105, 5.4 Control Flow.
#  Date:  10/27/2016 7pm - 12am, 45m break for dinner.
#  Memo:  Practice basic looping and syntax in R.
#
#  Printing works on older version RStudio.exe v.98x. Margin & Zoom too!
#----------------------------------------------------------------------------

#  Example 1:
#  if (cond) statement 
#  if (cond) statement1 else statement2   
#  ifelse(cond, yes, no)

x <- c(-15:15)
if (x[1] %% 3 == 0) print("Fizz")
if (x[6] %% 5 == 0) print("Buzz") else print(x[6])

#  Yes or No values automatically printed. No print() function needed.
#  Notice: not 'print("Fizz")' but just "Fizz" for yes statement.

x <- c(1:15)
ifelse(x[6] %% 3 == 0, y <- "yes", x[6])
ifelse(x[5] %% 5 == 0, "Buzz", x[5])
ifelse(x[7] %% 5 == 0, "Buzz", x[7])

#  Example 2:
#  for (i in sequence) expression
#  
#  for (i in 1:10) {
#    multiple lines
#  }

x <- (1:20)
for (i in x)
  if (x[i] %% 3 == 0) print("Fizz") else print(x[i])

for (i in 1:20)
  if (i %% 3 == 0) print("Fizz") else print(i)

#  i takes on values of sequence, even strings.
for (i in c(1, 2, 3, "hello", "me", "good", 7, 8, 9, "great"))
  print(i)

#  Spaces around all algebraic operators.
#  Curly braces, first on same line, last on new line. 2nd... indent 2 spaces.
#  Don't need curly braces for 1 line block following 'if'. Be consistent.

for (i in 1:30) {
  if (i %% 15 == 0) { 
    print("FizzBuzz") 
  } else {
    if (i %% 3 == 0) {
      print("Fizz")  
    } else {
      if (i %% 5 == 0){
        print("Buzz")
      } else {
        print(i)
      }  
    }  
  }
}

#  Example 3:
#  while (cond) statement

i <- 1
while (i < 22) {
  print(i)
  print(i*i)
  i <- i+2
}

#  while (i > 0) {do1; do2; do3} Notice semicolons separating statements.
i <- 1
while (i < 20) {print(i); print(i*i); i <- i+1}

#  Example 4:
#  switch(i, value1 = outcome1, value2 = outcome2, ...)
#  
#  switch(i,
#    value1 = outcome1,
#    value2 = outcome2, ...
#  )

with(Dataset, lineplot(V1, V2))
with(Dataset, Dotplot(V1, bin=FALSE))
scatterplot(V2~V1, reg.line=FALSE, smooth=FALSE, spread=FALSE, boxplots=FALSE, span=0.5, 
  ellipse=FALSE, levels=c(.5, .9), data=Dataset)
scatterplot(V2~V1, reg.line=FALSE, smooth=FALSE, spread=FALSE, boxplots=FALSE, span=0.5, 
  ellipse=FALSE, levels=c(.5, .9), data=Dataset)

print(x)

