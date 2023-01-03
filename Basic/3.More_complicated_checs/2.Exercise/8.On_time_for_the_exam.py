exam_hour = int(input())
exam_minutes = int(input())

arrival_hour = int(input())
arrival_minutes = int(input())

total_exam_minutes = exam_hour * 60 + exam_minutes
total_arrival_minutes = arrival_hour * 60 + arrival_minutes

first_output = ""
second_output = ""

if total_exam_minutes - total_arrival_minutes > 30:
    first_output = "Early"
    difference = total_exam_minutes - total_arrival_minutes
    if difference < 60:
        minutes = difference
        second_output = f"{minutes} minutes before the start"
    else:
        hours = difference // 60
        minutes = difference % 60
        if minutes <= 9:
            second_output = f"{hours}:0{minutes} hours before the start"
        else:
            second_output = f"{hours}:{minutes} hours before the start"
elif total_exam_minutes - total_arrival_minutes >= 0:
    first_output = "On time"
    if total_exam_minutes - total_arrival_minutes == 0:
        pass
    else:
        minutes = total_exam_minutes - total_arrival_minutes
        second_output = f"{minutes} minutes before the start"
else:
    first_output = "Late"
    difference = abs(total_exam_minutes - total_arrival_minutes)
    if difference < 60:
        minutes = difference
        second_output = f"{minutes} minutes after the start"
    else:
        hours = difference // 60
        minutes = difference % 60
        if minutes <= 9:
            second_output = f"{hours}:0{minutes} hours after the start"
        else:
            second_output = f"{hours}:{minutes} hours after the start"

print(first_output)
if total_exam_minutes - total_arrival_minutes == 0:
    pass
else:
    print(second_output)
