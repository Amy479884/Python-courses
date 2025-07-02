def powerof4(n):
    count = 0
    if (n & (~(n-1)) == n):
        while n>1:
            n >>= 1
            count +=1

        if count%2 == 0:
            return 1
        else:
            return 0

number=int(input("Enter a number:"))

if(powerof4(number)):
    print("The number is power of 4")
else:
    print("The number is not power of 4")