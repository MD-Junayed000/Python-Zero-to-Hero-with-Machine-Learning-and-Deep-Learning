# exception = An event that interrupts the flow of a programme
#             (ZeroDivision 1/0 , TypeError 1+'1' , ValueError  int('string') )
#             1.try # try some code , 2.except #Handle an Exception ,3. finally # Do some clean up

try:

    number=int(input('Enter a number: '))
    print(1/0)

except  ZeroDivisionError:
    print('You Cannot Divide by Zero Idiot')

except ValueError:
    print('Enter only numbers please')

##### Catch all exception

except Exception:
    print('All general purpose error')

finally:
    print('Do some clean up here')


### Raise Custom Error

a=int(input('Enter a Value between 5 to 9: '))

if (a<5 or a>9):
    raise ValueError('You have enter value that is out of range')





