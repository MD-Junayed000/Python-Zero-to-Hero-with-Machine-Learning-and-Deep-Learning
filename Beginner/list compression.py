# list compression = A concisee way to create list in python
##                   Compact and easier to read than traditional loops
#                    [expression for value in iterable if condition]

doubles=[]
for x in range(1,11):
    doubles.append(x*2)

print(doubles)

#### in more shortcut way

tri=[x*3 for x in range(1,11)]

print(tri)

###################################
fruits=['aaple','orange','banana','cola']
fruits=[fruit.upper() for fruit in fruits]
print(fruits)

###############################################

fruits=[fruit.upper() for fruit in ['aaple','orange','banana','cola']]
print(fruits)

####### ony the 1st character

fruits=[ fruit[0] for fruit in ['mango','jack','blossom'] ]
print(fruits)


#### with if condition
numbers=[-1,-4,--2,5,9,0,-2]
positive_num=[num for num in numbers if num>=0]
odd=[num for num in numbers if num%2!=0]
print(positive_num)
print(f'odd is {odd}')

################################################





def day_of_week(day):
    if day==1:
        print('Sunday')

    elif day==6:
        print('JUNu')

    else:
        print('not in calender')

print(day_of_week(4))

#  or ======= |

