# multi-threading = Used to perform multiple tasks concurrently (multitasking)
#                   Good for I/O bound tasks like reading files
#                   or fetching data from API's threading .Thread(target=my_function)

import threading
import time

def walk_dog(name,last):
    time.sleep(8)
    print(f'You finish walking the dog: {name}>>>{last}')

def take_out_trash():
    time.sleep(2)
    print('You take out on the trash')

def get_mail():
    time.sleep(4)
    print('You get the mail')
## Normal function dile will work serially thus take a lot of time
### but there time dependent
chore1=threading.Thread(target=walk_dog,args=('JUNU','INKI'))
chore1.start()

chore2=threading.Thread(target=take_out_trash)
chore2.start()


chore3=threading.Thread(target=get_mail)
chore3.start()


print('All chores are complete')