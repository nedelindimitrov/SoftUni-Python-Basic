budget = int(input())
season = input()
fishermen_count = int(input())

price = 0

#first discount for the season
if season == "Spring":
    price = 3000
elif season == "Summer" or season == "Autumn":
    price = 4200
elif season == "Winter":
    price = 2600

#second discount for the fishermen count
if fishermen_count <= 6:
    price *= 0.9
elif fishermen_count <= 11:
    price *= 0.85
elif fishermen_count >= 12:
    price *= 0.75

#third optional discount
if fishermen_count % 2 == 0 and season != "Autumn":
    price *= 0.95

if budget >= price:
    print(f"Yes! You have {budget - price:.2f} leva left.")
else:
    print(f"Not enough money! You need {price - budget:.2f} leva.")
