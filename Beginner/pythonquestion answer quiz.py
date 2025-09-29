#python quiz game

questions= ("How many elements are there in periodic table?: ",
           "BD is known for which animal?: ",
           'we breath which gas?: ',
           "How many bones are there in human body?: ",
           'we live in which planet')

options=(("A.116",'B.117','C.118','D.119'),('A.Lion','B.Scorpion','C.Tiger','D.Liger'),('A.Nitrogen','B.Oxygen','C.Carbon','D.Metal'),('A.217','B.Penis','C.420','D.5271'),('A.Earth','B.Mars','C.Zuko','D.Amagas'))

answers = ('C','C','B','A','A')

guesses = [] # append element in guesses so use list

score=0
question_num=0

for question in questions:
    print("------------------------------------")

    print(question)

    for option in options[question_num]:
        print(option)

    guess=input("Enter the correct answer: ").upper()
    guesses.append(guess)

    ####    if guesses[question_num]==answer[question_num]:
    if guess == answers[question_num]:
        print('Correct')
        score+=1

    else:
        print('Incorrect')


    print()
    print(f'{answers[question_num]} is the correct answer')



    question_num+=1
print('---------------------------------------------')
print('Result')
print('---------------------------------------------')

print('Correct answer: ',end='')
for answer in answers:
    print(answer,end=' ')

print()
print('Your guesses: ')

print(guesses)



print(f'Your score is: {score}')

score=int((score/len(questions))*100)
print(f'In percentage: {score}%')






