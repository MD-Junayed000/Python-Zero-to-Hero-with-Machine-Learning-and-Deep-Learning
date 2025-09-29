import time

time.sleep(3) # count in sec
### thus the code will be executed after 3 sec// will be sleep for 3 sec
print('Times up Boy')


### Demo
my_time= int(input("Enter the time in second: "))

for x in range(0,my_time): # if done in reverse reversed(range(0,my_time)) ///  range(my_time,0,-1)
    print(x)
    time.sleep(1)# after each 1 sec

print("Hurray!")




### Implementation
### Demo
my_time= int(input("Enter the time in second: "))

for x in range(my_time,0,-1): # if done in reverse reversed(range(0,my_time)) ///  range(my_time,0,-1)
    seconds= x%60 ## as modulus lower then it will not be affected
    # here modulus er niche jara will not be affected
    minutes=int(x/60 )% 60

    hours=int(x/3600)  ## modulus (% 60) diy nai as the 60 hr por por reset hye jbe and it's not possible

    print(f"{hours:02}:{minutes:02}:{seconds:02}")

    time.sleep(1)# after each 1 sec

print("Times up!")



