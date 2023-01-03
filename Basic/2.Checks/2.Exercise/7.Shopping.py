peter_budget = float(input())

videocard_price = 250
videocard_count = int(input())

videocard_sum = videocard_count * videocard_price

processor_price = videocard_sum * 0.35
processor_count = int(input())

processor_sum = processor_count * processor_price

ram_price = videocard_sum * 0.10
ram_count = int(input())

ram_sum = ram_count * ram_price

total_sum = videocard_sum + processor_sum + ram_sum

if videocard_count > processor_count:
    total_sum *= 0.85

if peter_budget >= total_sum:
    print(f"You have {peter_budget - total_sum:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_sum - peter_budget:.2f} leva more!")
