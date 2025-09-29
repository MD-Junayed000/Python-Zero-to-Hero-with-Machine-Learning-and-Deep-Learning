# shopping cart programme
##not using tuple as unchanglable and we need input
## not set as unordered
foods=[]
prices=[]
total=0

while True:
    food=input('Enter a food to buy (q to Quit): ')

    if food.lower()=='q':
        break
    else:
        price = float(input(f'Enter the price of a {food}: $ '))
        foods.append(food)
        prices.append(price)

print('------Your Cart -------------')
for i in range(len(foods)):
    print(f"{foods[i]} - ${prices[i]:.2f}")
    total += prices[i]
print()
print(f'Your total price is {total:.2f}$')

