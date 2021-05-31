#This is the implementation of an alarm in python 3.7.1

import time 
import winsound
from win10toast import ToastNotifier


def timer(mess, minutes):
    notificator = ToastNotifier()
    notificator.show_toast("Alarm",
              f"Alarm will ring in {minutes} minutes....", duration=50)
    time.sleep(minutes * 60)
    winsound.Beep(frequency=2500, duration=1000)
    notificator.show_toast(f"Alarm", message, duration=50)

if __name__ == '__main__':
    message = "wake up"
    minutes = 60
    timer(message, minutes)