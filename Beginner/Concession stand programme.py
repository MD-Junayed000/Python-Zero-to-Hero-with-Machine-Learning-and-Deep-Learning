#    Concession stand programme

menu={ 'pizza': 3.00,
       'burger':6.75,
       'cola':1.24,
       'chips':1.00,
       'lemonade':4.25
}

cart=[]
total=0

print('-------------------MENU---------------------------')

for key,value in menu.items():
       print(f'{key:10}: ${value:1f}')

print('--------------------------------------------------')

while True:
       food=input('Select an item(q to quit): ').lower()
       if food=='q':
              break
       elif menu.get(food) is not None: ## exist
              cart.append(food)

print(cart)



for food in cart:
       print(menu.get(food)) #### get method is always with Dictionary
       total+=menu.get(food)


print(f"Total is : ${total}")

















