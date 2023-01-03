film_budget = float(input())
statist_number = int(input())
price_clothes_per_statist = float(input())

decor = film_budget * 0.10
clothes = statist_number * price_clothes_per_statist

if statist_number > 150:
    clothes *= 0.90

total_expenses = clothes + decor

if film_budget >= total_expenses:
    print("Action!")
    print(f"Wingard starts filming with {film_budget - total_expenses:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {total_expenses - film_budget:.2f} leva more.")
