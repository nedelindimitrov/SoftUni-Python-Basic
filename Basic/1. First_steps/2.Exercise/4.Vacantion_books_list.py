pages_to_read = int(input())
pages_per_hour = int(input())
days = int(input())

total_hours = int(pages_to_read / pages_per_hour)
hours_per_day = int(total_hours / days)
print(hours_per_day)
