print("First activity")
num=23
print("Table of 23")
for i in range(1,11):
    mul = num*i
    print("23*%d=%d" % (i, mul))

print("\n")

print("This is the second activity")
n = int(input("enter number of rows"))

for i in range(0, n):

	for j in range(0, i+1):
		print("*", end=" ")

	print("\n")

print("This is the third project")
number=1
sum=0
while(num<=17):
	sum=sum+number
	number= number+1
print("Sum of the first 10 natural numbers:" , sum)

print("\n")
print("This is the forth activity")
num = int(input("Enter number to be checked :"))

flag = False

if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")


	

