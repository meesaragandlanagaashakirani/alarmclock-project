from datetime import datetime
from playsound import playsound
import time

alarm_time = input("Enter alarm time (HH:MM:SS): ")

while True:
    current_time = datetime.now().strftime("%H:%M:%S")

    print("Current Time:", current_time)

    if current_time == alarm_time:
        print("WAKE UP!")
        playsound("alarm.wav")
        break

    time.sleep(1)
