from math import ceil

serial_name = input()
episode_duration = int(input())
break_duration = int(input())

lunch_time = break_duration / 8
rest_time = break_duration / 4

free_time = break_duration - lunch_time - rest_time

if free_time >= episode_duration:
    print(f"You have enough time to watch {serial_name} and left with {ceil(free_time - episode_duration)} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, you need {ceil(episode_duration - free_time)} more minutes.")
