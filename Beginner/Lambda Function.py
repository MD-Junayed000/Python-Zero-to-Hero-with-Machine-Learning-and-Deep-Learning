## def double(x):
#  return x*2


double=lambda x: x*2
print(double(5))

avg=lambda x,y,z: (x+y+z)/2
print(avg(5,3,9))

## we can pass function to another function

def appl(fx,value):
    return 6+ fx(value)

print(appl(double,30))###