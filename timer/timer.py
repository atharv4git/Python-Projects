import time
from playsound import playsound

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        hrs = int(mins/60)
        timeformat = '{:02d}:{:02d}:{:02d}'.format(hrs, mins ,secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    playsound("alarm.mp3")
    print("stop")

mins = int(input("enter the mins you want:"))
countdown(mins*60)
