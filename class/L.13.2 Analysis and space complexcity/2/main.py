def sum(n):
    return n*(n+1)/2

def arraysum(a):
    sum=0
    for i in a:
        sum=sum+i

    return(sum)
a = [12,3,4,15]
arraysum(a)

def sum(n):
    if(n<=0):
        return
    return n+sum(n-1)

