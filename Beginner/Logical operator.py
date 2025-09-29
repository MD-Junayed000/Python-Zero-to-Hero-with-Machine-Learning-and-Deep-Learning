##Temp

temp=25
is_raining=False

if temp>35 or temp<0 or is_raining:# By default is True
    print("Will not go")

else:
    print("Will go there")

#Conditional Expression: x if condition else y
num=5
print("Positive"if num>0 else "Negetive")

num=6
result="Even" if num%2==0 else "ODD"
print(result)

##
user_role="guest"
access_level= "Full Access" if user_role=="admin" else "Limited Access"
print(access_level)

