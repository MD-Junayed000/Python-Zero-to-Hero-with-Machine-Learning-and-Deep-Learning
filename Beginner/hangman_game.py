## Hangman game

## sets of words will be choosen at random and guess it one at a time with six incorrect guessess we will loose the game

import random

words=('apple','orange','banana','coconut','pineapple')

# dictionary of key:() ---tuple

hangman_art={ 0:('     ',
                 '     ',
                 '     '),
              1:('  o  ',
                 '     ',
                 '     '),
              2:('  o  ',
                 '  |  ',
                 '     '),
              3:('  o  ',
                 ' /|  ',
                 '     '),
              4:('  o  ',
                 ' /|\ ',
                 '     '),
              5:('  o  ',
                 ' /|\  ',
                 ' /    '),
              6:('  o  ',
                 ' /|\  ',
                 ' / \  ')
}


print(hangman_art[0])  #####represent no in-correct guessess

print(hangman_art[0])

for line in hangman_art[6]:
    print(line)


def display_man(wrong_guesses):
    print('****************************')
    for line in hangman_art[wrong_guesses]:
        print(line)
    print('***************************')

def display_hint(hint):
    print(' '.join(hint))

def display_answer(answer):
    print(' '.join(answer))

def main():
    answer=random.choice(words)
    print(answer)
    hint=['_']*len(answer)
    print(hint)
    wrong_guesses=0
    guessed_letter=set()  ### list empty [] but in empty set we need set()
    is_running=True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess= input('ENter a letter: ').lower()

        if len(guess)!=1 or not guess.isalpha():
            print('Invalid length')
            continue



        if guess in guessed_letter:
            print(f'{guess} is already guessed')
            continue

        guessed_letter.add(guess) #### porre dite hbe as 1st time no second bar dewa




        if guess in answer:
            for i in range(len(answer)):
                if answer[i]==guess:
                    hint[i]=guess

        else:
            wrong_guesses+=1

        if '_' not in hint: #### win
            print('You win')
            is_running= False

        if wrong_guesses>=len(hangman_art)-1: #### as 1st a null condition
            print('you loose')
            is_running=False




if __name__=='__main__':
    main()






