# nested loop- A loop within another loop (outer,inner)
#                  outer loop:
#                           inner loop

## for print in smae line print(x, end='')
## normally print ekta por ekta as by defult print(x,end='\n')

for x in range(1,10):
    print(x,end='') # no space

for x in range(3):
    for y in range(1, 10):
        print(y, end=' ')  # no space
    print() ### print a new line


