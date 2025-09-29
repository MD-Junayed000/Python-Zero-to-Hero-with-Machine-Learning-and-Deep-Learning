
import math
cube= lambda x: math.pow(x,3)

l=[1,2,3,4,6,4,3]
'''newl=[]

for item in l:
    newl.append(cube(item))'''

newl=list(map(cube,l))

print(newl)


