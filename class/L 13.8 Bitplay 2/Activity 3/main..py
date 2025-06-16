def printtwonum(arr,length):
    result=arr[0]
    x=0
    y=0
    setbit=0
    for i in range(1,length):
        result=result^arr[i]
        setbit=result&~(result-1)

    for i in range(length):
        if(arr[i]&setbit):
            x=x^arr[i]
        else:
            y=y^arr[i]
    print("the 2 odd element are:",x, "and",y)



arr=[]
n=int(input("how many numbers do you want:"))
for i in range(0,n):
    z=int(input("enter number:"))
    arr.append(z)
printtwonum(arr,n)