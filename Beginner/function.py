# function-- A block of reusable code
#            place () after the function name to invoke it


def happy_birthday(name,age):
    for i in range(1,4):
        print(f'Happy Birthday {name}')
        print()
        print(f'you are {age} years old')

happy_birthday('Junu',20)

######################################################
# return == statement used to end a function
#            and send a result back to the caller

def add(x,y):
    z=x+y
    return z
def subtract(x,y):
    z=x-y#
    return z
def multiply(x,y):
    z=x*y
    return z

print()
print(add(1,2))



#### Capitalize the Full name
def create_name(first,last):
    first=first.capitalize()
    last=last.capitalize()
    return first+ ' '+last

full_name=create_name('junu','naomi')
print(full_name)













