# collection = single 'variable' used to store multiple values
# list= [] # square bracket # ordered and changeable. Duplicates OK
# set= {} # curly bracket # unordered and immutable, but ADD/Remove ok. No Duplicates are allowed
# tuple= () # parenthesis # order and unchangable. Duplicates ok. Faster than list

fruits= ['apple','banana','mango','litchi']
print(fruits[1]) # indexing

print(fruits[::2]) # show after every two element
# in reverse
print(fruits[::-1])

for fruit in fruits:
    print(fruit)#

print()
## Bolean
print('apple'in fruits)

# replace specific indexing
fruits[0]= 'pineapple'
print(fruits)



## append at the end of the list
fruits.append('jackfruit')
print(fruits)

# inserting indexing and pushing
fruits.insert(1,'rasmerry')
print(fruits)

## remove
fruits.remove('mango')
print(fruits)

## sort method sorts list by default in alphabetical order for string
fruits.sort()
print(fruits)
# to return index of an element
print(fruits.index('jackfruit'))

## to count Frequency / Duplicates use count

print(fruits.count('banana'))




## to clear everything
fruits.clear()



########### SETTT ###########
### each time run is in different order #############
fruits= {'apple','banana','mango','litchi'}

print(fruits)


print(fruits[0])

## set e add and remove kaj kre
# fruits.add('')
### pop() method will remove which evver element comes 1st
## but in set it is random
fruits.pop()
print(fruits)

# clear all
# fruits.clear()


