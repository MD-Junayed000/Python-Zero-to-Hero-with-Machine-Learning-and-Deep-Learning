##### Random Number
import random


low=1
high=100
options=('rock','paper','scissor')
cards=['2','4','A','6','Q']
# number= random.randint(low,high)
# number=random.random() #random floating point
option=random.choice(options)
print(option)

##shuffle the sequence
random.shuffle(cards)
print(cards)

##### Random guessing of NUmber

low=0
high=100
answer=random.randint(low,high)
guesses=0
is_running=True

print('Python Number guessing Game')
print(f"Select a number between {low} and {high}")

while is_running:
    guess=input("Enter a Number: ")

    if guess.isdigit():
        guess=int(guess)
        guesses+=1
        if guess<low or guess>high:
            print('Not in range')
            print(f"Select a number between {low} and {high}")

        elif guess<answer: # Borabor mile nai
            print('Incorrect and low')

        elif guess>answer:
            print('Incorrect and high')

        else:
            print('Correct')
            print(f"Took number of guesses: {guesses}")
            is_running=False
    else:
        print("Invalid Input")
        print(f"Select a number between {low} and {high}")


















