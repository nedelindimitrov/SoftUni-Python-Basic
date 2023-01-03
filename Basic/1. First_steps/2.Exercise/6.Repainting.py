plastic_price = 1.50
paint_price = 14.50
thinner_price = 5

plastic_needed = int(input())
paint_needed = int(input())
thinner_needed = int(input())
hours = int(input())

plastic_expenses = (plastic_needed + 2) * plastic_price
paint_expenses = (paint_needed + (paint_needed * 0.10)) * paint_price
thinner_expenses = thinner_needed * thinner_price
bags_expenses = 0.40

all_expenses = plastic_expenses + paint_expenses + thinner_expenses + bags_expenses
workers_expenses_per_hour = all_expenses * 0.30
workers_total_expenses = workers_expenses_per_hour * hours

total_sum = workers_total_expenses + all_expenses

print(total_sum)
