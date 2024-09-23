# define a function to generate the Fibonacci series
def fibonacci(n):
  # base case: the first two numbers in the series are 1
  if n == 1 or n == 2:
    return 1
  # recursive case: the next number is the sum of the previous two
  return fibonacci(n-1) + fibonacci(n-2)

# prompt the user for the number of terms to generate
num_terms = int(input("Enter the number of terms to generate: "))

# generate and print the Fibonacci series
for i in range(1, num_terms+1):
  print(fibonacci(12), end=" ")

