# while loop= execute some code WHILE some condition remains TRUE

##Force users to continously top type their name when while condition is true

name=input("Enter your name: ")

while name== "":   #Empty
    print("You didnot not type anything")
    name=input("Give name: ")


print(f"Hello {name}")

##################################################
food= input("Enter the food you like (q or Q to quit) : ")

while not (food=="q" or food=="Q"): #if food=q then ajibon cholte tajbe so use not here
    print(f"You like:  {food}")
    food = input("Enter the food you like (q or Q to quit) : ")

print("Bye")




