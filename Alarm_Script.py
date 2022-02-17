#!/usr/bin/env python3
import datetime
import os

set_alarm_time = False
print("Let's set your alarm!")
hour_input = input("HOUR: \n")
minute_input = input("MINUTE: \n")
ampm_input = input("AM or PM? \n")

#input validation
# if len(alarm_input) == 8:
#     if alarm_input[6:] == "AM" or alarm_input[6:] == "PM":

#Converting alarm_input into time object. Assume input is valid.
if ampm_input == 'AM':
    hour_input = int(hour_input)
    alarm_time = datetime.time(hour_input, int(minute_input), 0)
if ampm_input == 'PM':
    hour_input = int(hour_input)
    hour_input += 12
    alarm_time = datetime.time(hour_input, int(minute_input), 0)
set_alarm_time = True
print("Your alarm has been set! >:)")
#curr_hour = 0
#curr_minute = 0
while set_alarm_time:
    curr_time = datetime.datetime.now()
    timestamp = curr_time.strftime('%H:%M:%S')
    curr_hour = int(timestamp[:2])
    curr_minute = int(timestamp[3:5])
    if curr_hour == alarm_time.hour and curr_minute == alarm_time.minute:
        print("WAKEUP")
        #os.startfile('videoplayback.mp4')