record_to_beat = float(input())
meters = float(input())
seconds_needed_for_meter = float(input())

first_time = meters * seconds_needed_for_meter
adding_time = (meters // 15) * 12.5
total_time = first_time + adding_time

if total_time < record_to_beat:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {total_time - record_to_beat:.2f} seconds slower.")
