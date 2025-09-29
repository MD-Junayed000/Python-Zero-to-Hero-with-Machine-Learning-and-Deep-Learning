marks=[33,56,32,98,12,45,1,4]
'''index=0
for mark in marks:
    print(mark)
    if index==3:
        print('Junayed is awesome')
    index+=1'''

for index,mark in enumerate(marks):
    print(mark)
    if index == 3:
        print('Junayed is awesome')
    # index += 1

print('######################################')

fruits=['banana','juice','litchi','drinks']

for index,fruit in enumerate (fruits,start=1): ## shows the starting of index
    print(index,fruit)

