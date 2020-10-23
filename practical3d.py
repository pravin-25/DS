# using recursion
def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num =12

if num < 0:
   print("Number is negative")
elif num == 0:
   print("The factorial is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))



#using iteration 
def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

num = 12

print_factors(num)