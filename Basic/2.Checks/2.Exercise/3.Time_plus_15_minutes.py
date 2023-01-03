hours = int(input())
minutes = int(input())

total_minutes = hours * 60 + minutes + 15

hours = total_minutes // 60
minutes = total_minutes % 60

if minutes <= 9:
    if hours == 24:
        print(f"0:0{minutes}")
    else:
        print(f"{hours}:0{minutes}")
else:
    if hours == 24:
        print(f"0:{minutes}")
    else:
        print(f"{hours}:{minutes}")
