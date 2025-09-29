#                     1. positional 2.default 3. keyword 4. arbitrary


# default arguments = A default value for certain parameters
#                     default is used when argument is omitted
#                     make your function more flexible ,reduces # of arguments



## Calculate net price

def net_price(list_price,discount=0,tax=0.05): ## kicchu nh dile default argument
    return list_price*(1-discount)*(1+tax)

#print(net_price(500))
print(net_price(500,0.1,))


## make counter
import time
def count(start,end):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)

    print('Done!')

count(2,8)


# keyword arguments= an argument preceded by an identifier
#                    helps with readability
#                    order of argument doesnot matter


print('1','2','3','4','5',sep='-')


# *args ---tupple() == allow you to pass multiple non-key arguments
# **kwargs --- dictionary {} == allow you to pass multiple keyword-arguments
#                                * unpacking operator


def add(*args): ###############  *num
    print(type(args))
    total =0
    for arg in args:
        total+=arg
    return total

print(add(1,2,3))



def display_names(*nums):
    for num in nums:
        print(num,end=' ')


display_names('junu','Fucking','pants')

print()
## **kwargs

def print_address(**kwargs):
    print(type(kwargs))
    for key,value in kwargs.items(): ## kwargs.keys() //// kwargs.values()
        print(f'{key}-----{value}')


print_address( street='Califona',
               city='Westron',
               state='Merica',
               zip='4000')



## Exercise with args and kwargs

def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg,end=' ')

    print()

    if 'apt' in kwargs:
        print(f"{kwargs.get('street')} and {kwargs.get('apt')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"also {kwargs.get('zip')}")



shipping_label('junu','nuu','nezz',
               street='chattogram',
               apt='Brainstation23',
               zip='4000'
)