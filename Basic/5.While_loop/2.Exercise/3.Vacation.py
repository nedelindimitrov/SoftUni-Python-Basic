money_needed = float(input())

her_total_money = float(input())

days_spending = 0
total_days = 0

while True:
    if days_spending == 5:
        print(f"You can't save the money.")
        print(total_days)
        break
    operation = input()
    if operation == "spend":
        current_sum = float(input())
        days_spending += 1
        total_days += 1
        her_total_money -= current_sum
        if her_total_money <= 0:
            her_total_money = 0
    elif operation == "save":
        current_sum = float(input())
        days_spending = 0
        total_days += 1
        her_total_money += current_sum
        if her_total_money >= money_needed:
            print(f"You saved the money for {total_days} days.")
            break
