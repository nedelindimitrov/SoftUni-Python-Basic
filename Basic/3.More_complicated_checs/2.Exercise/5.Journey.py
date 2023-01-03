budget = float(input())
season = input()

destination = ""
rest_type = ""
money_spent = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        rest_type = "Camp"
        money_spent = budget * 0.30
    elif season == "winter":
        rest_type = "Hotel"
        money_spent = budget * 0.70
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        rest_type = "Camp"
        money_spent = budget * 0.40
    elif season == "winter":
        rest_type = "Hotel"
        money_spent = budget * 0.80
else:
    destination = "Europe"
    rest_type = "Hotel"
    money_spent = budget * 0.90

print(f"Somewhere in {destination}")
print(f"{rest_type} - {money_spent:.2f}")
