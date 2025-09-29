#dictionary = a collection of {key:value} pairs
#             ordered and changable . No duplicates

## like set {......}

capitals={"USA": "Washington DC",
          "India": "Delhi",
          "Bangladesh": "Dhaka",
          "Isreal": "Jerusalem"}

## to get the value of specific key use the .get() method

print(capitals.get('USA'))

##also to check is a key exist in dictionary we can use the .get() method

if capitals.get("Japan"):
    print('Capita exist')

else:
    print('Not in the dictionary')


capitals.update({'Russia':'Moscow'})
capitals.update({'Bangladesh':"Islamabad"}) # update existing key's value
print(capitals)

## remove using the .pop() method

capitals.pop("India")
print(capitals)

##to remove the last key use popitem() even without inserting the key

capitals.popitem()
print(capitals)

#capitals.clear()

#to get only all the keys not it's corresponding value use the keys method
keys=capitals.keys()
print(keys)


##only iterate through the key
for i in capitals:
    print(i)

print("######################")
#####
items= capitals.items()
print(items)

###################################

print()
for key,value in capitals.items():
    print(f'{key}: {value}')