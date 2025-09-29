# 2d list=[list1,list2,list3]
# Grid / Matrix of Data
from Tools.scripts.highlight import default_latex_document

#foir 2Dlist we need to create1D first

fruits=["apple",'orange','banana','coconut']
vegetables=['celery','carrots','potatoes']
meats=['chicken','fish','turkey']

groceries=[fruits,vegetables,meats]
fruits[0]='pineapple'
print(fruits)

print()
print(groceries[1])#represent entire rows
print(groceries[0][2])#banana #)### each index represnt [row]'[column]


############################
#short explanation
matrix=[['junu','nunu','hell'],
        ['seth','rollins','seam'],
        ['ola','fucknitosh','gre']]

print(matrix[1])

print()

#############

#if need to iterate over the 2D list we need to use the Nested loop

for collection in groceries:
        print(collection) # Iterate just over the rows

for collection in groceries:
        print()
        for every_food in collection:
                print(every_food)


##     Exercise        ###########

##          2D keypad normally found on phone

# set unorderable
# tupple fast and unchangeable

# so in keypad it might be the best option

num_pad= ((1,2,3),(4,5,6),(7,8,9),('*',0,'#'))

for row in num_pad:
        for column in row:
                print(column,end=' ')
        print()
















