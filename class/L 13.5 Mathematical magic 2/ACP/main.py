# Find all prime numbers having 2 digits

def is_prime(num):
    if num<2:
      return False
    for i in range(2,int(num**0.5)+1):
      if num %i==0:
       return False
    return True
      

two_digit_prime = [num for num in range(10,100) if is_prime(num)]
print(two_digit_prime)