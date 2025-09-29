## Calling a Function inside another function


# let factorial (7)= 7*6*5*4*3*2*1
# factorial(0)=1
# factorial (n)=n* factorial(n-1)

def factorial(n):
    if (n==0) or (n==1):
        return 1
    else:
        return n * factorial(n-1)

fac=factorial(1)
print(fac)
