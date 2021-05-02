import datetime
from playsound import playsound
alarmhour=int(input('Enter hour: '))
alarmmin=int(input('Enter minute: '))
alarm_am_pm=input('Enter AM or PM: ')

if alarm_am_pm=='PM' or 'pm' or 'Pm' or 'pM':
    alarmhour+=12

while True:
    if alarmhour==datetime.datetime.now().hour and alarmmin==datetime.datetime.now().minute:
        print('Playing..')
        playsound("alarm_tune.mp3")
        break