# if= Do some code only if condition is True
#     else do something else

age =int(input("Enter the age: "))
if age>=18:
    print("Eligible")

elif age<0:
    print("Chudu")

elif age>=100:
    print("HAnki") ## not working as First condition is met

else:
    print("Fuck me")



    ###################################


name=input("Enter your name: ")

if name=="":
        print("u did not type anything")

else:
        print(f"fuck u {name}")


# bolean is by default==True

sale=False
if sale: #if True then execute
    print("Hurray")

else:
    print("Baalllll")

# Python Calculator

weight=float(input("Enter weight: "))
unit= input("Kilograms or pounds? (k or l): ")

if unit=="k":
    weight*=2.205
    unit="Lbs"
elif unit=="l":
    weight/=2.205
    unit="kgs"
else:
    print(f"{unit} was not valid")

print(f"Your weight is : {round(weight,2)} {unit}")