
###########################################################

principle=0 #Initial amount
rate=0 # rate of interest
time=0 # time period mainly in years

while True:
    principle=float(input("Enter the Principle Amount: "))
    if principle<0:
        print("Invalid amount")
    else:
        break

