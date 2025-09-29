# membership operator = used to test whether a value or variable is found in a sequence
#                     (string,list,tuple,set,or dictionary)
#                      1.in
#                      2. not in

word='APPLE'

letter=input('Enter a letter in the secret word: ').capitalize()

if letter in word:
    print(f'There is a {letter}')

else:
    print('Invalid')


### In Iterable for dictionary for the key can be accessible

grades={'Junu':'A',
        'Yeasmin':'F',
        'Adi':'B'
}

student=input('Enter the name of the studnet: ')

if student in grades:
    print(f'{student} grades is {grades[student]}')

else:
    print(f'{student} not found in tje dictionary')




