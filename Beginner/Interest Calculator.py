# Python Compound Interest Calculator

principle=0 #Initial amount
rate=0 # rate of interest
time=0 # time period mainly in years

while principle <=0:
    principle=float(input("Enter the Principle Amount: "))
    if principle<=0:
        print("Invalid amount")


while rate <=0:
    rate=float(input("Enter the rate of interest: "))
    if rate<=0:
        print("Invalid amount")


while time <=0:
    time=float(input("Enter the time: "))
    if time<=0:
        print("Invalid amount")

total= principle*pow((1 + rate/100),time)
print(f"Balance after{time} years is : ${total:.2f}")

########################################################

### in more easy way (can also take zero now)

# Python Compound Interest Calculator

principle=0 #Initial amount
rate=0 # rate of interest
time=0 # time period mainly in years

while True:
    principle=float(input("Enter the Principle Amount: "))
    if principle<0:
        print("Invalid amount")
    else:
        break


while True:
    rate=float(input("Enter the rate of interest: "))
    if rate<0:
        print("Invalid amount")
    else:
        break


while True:
    time=float(input("Enter the time: "))
    if time<0:
        print("Invalid amount")
    else:
        break

total= principle*pow((1 + rate/100),time)
print(f"Balance after{time} years is : ${total:.2f}")

