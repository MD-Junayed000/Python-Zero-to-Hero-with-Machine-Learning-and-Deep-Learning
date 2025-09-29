#for loop- execute a block of code a fixed number of times

# range(start,end-1# as exclude it)

for x in range(1,11):
    print(x)
#in reversed order
for counter in reversed(range(1,11)):
    print(counter)

print("Happy New Year")

card="2345-45456"
for x in card:
    print(x)


#to skip over the operation use the (continue keyword):

for x in range(1,6):
    if x==3:
        continue
    else:
        print(x)

# to get out of the loop use (break)
for x in range(1,6):
    if x==3:
        break
    else:
        print(x)


        