deposit_sum = float(input())
months = int(input())
annual_interest = float(input())
annual_to_calculate = annual_interest / 100

interest_per_year = deposit_sum * annual_to_calculate
interest_per_month = interest_per_year / 12
total_sum = deposit_sum + months * interest_per_month

print(total_sum)
