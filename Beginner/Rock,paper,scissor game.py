import random

options=['rock','paper','scissor']


running=True

while running:
    player = None
    computer = random.choice(options)

    ### to makle sure user input stays within that range
    while player not in options:

         player=input('Enter between rock and paper and scissor: ') ## Forcing to get bar bar input

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player==computer:
        print('Its a tie')

    # play_again=input('play again: (y/n): ').lower()
    # if not play_again=='y':
    if not input('play again: (y/n): ').lower()=='y':
        running=False



