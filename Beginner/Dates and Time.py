import datetime

date=datetime.date(2025,5,24)## yr....month......date


today=datetime.date.today()
print(today)
print('#############')
print(date)

time=datetime.time(12,45,23) # hr........min......sec
print(time)

## what is the time wright nowww

now=datetime.datetime.now()
print(now)

#####  See if current date time has passed our tageted date time

target_datetime=datetime.datetime(2025,1,2, 12,34,51) ##date followed by time

current_datetime=datetime.datetime.now()

if target_datetime< current_datetime:
    print('Target date has passed')

else:
    print('Target time has not passed')
#####################################################################

# Python Alarm Clock
import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f'Alarm Set for {alarm_time}')
    sound_file='heating-sun-327239.mp3'
    is_running=True

    while is_running:

        current_time=datetime.datetime.now().strftime('%H:%M:%S') ## string-format-time
        print(current_time)

        if current_time==alarm_time:
            print('Wake up Idiot!')



            pygame.mixer.init()### mixer is a module for loading and playing sound
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False


        time.sleep(1)








if __name__=='__main__':
    alarm_time=input('Enter the alarm time (HH:MM:SS): ')
    set_alarm(alarm_time)





















