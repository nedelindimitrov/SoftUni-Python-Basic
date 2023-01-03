time_first = int(input())
time_second = int(input())
time_third = int(input())

total_seconds = time_first + time_second + time_third
hours = total_seconds // 60
minutes = total_seconds % 60

if minutes <= 9:
    print(f"{hours}:0{minutes}")
else:
    print(f"{hours}:{minutes}")
