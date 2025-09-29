name=input("Enter ur name: ")
# result=len(name)
# print(result)


## First occurence of a position in a string is done by dot-find method(  .find()  )

result=name.find(" ") # one space find
print(result)

# last occurence will be rfind()
# couldnot find answer will be -1


another=input("Type anything: ")
another=another.upper() ## alkl string are capitalize
print(another)

# all lowercase== .lower()

#if string contains only digit return true or False
no1=another.isdigit()
print(no1)

# Count what u want by === count("xyz")
phn=input("Enter the number: ")
count=phn.count("-")
print(count)

replace=phn.replace("-","*")
print(replace)

##Exercise
#validate user ninput
# 1.username is no more than 12 characters
#2. usernbame must not contain spaces
#3. username must not contain digits


username= input("Enter a username: ")

username.find(" ") ## if there is no space means space not found== -1
# i.e cannot locate it
username.isalpha() ## return true if all string are alphabet

if len(username)>12:
    print("Length not valid")
elif not username.find(" ")==-1: ## thus if have spaces
    print("Space not valid")

elif not username.isalpha(): ## now by default false
    print("Digit not valid")
else:
    print("Valid")