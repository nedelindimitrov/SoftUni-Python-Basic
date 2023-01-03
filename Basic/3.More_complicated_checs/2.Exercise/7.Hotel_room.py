month = input()
nights = int(input())

price_per_night_studio = 0
price_per_night_apartment = 0

if month == "May" or month == "October":
    price_per_night_studio = 50
    price_per_night_apartment = 65
elif month == "June" or month == "September":
    price_per_night_studio = 75.20
    price_per_night_apartment = 68.70
elif month == "July" or month == "August":
    price_per_night_studio = 76
    price_per_night_apartment = 77

total_price_studio = nights * price_per_night_studio
total_price_apartment = nights * price_per_night_apartment

if nights > 14:
    total_price_apartment *= 0.90
    if month == "June" or month == "September":
        total_price_studio *= 0.80
    elif month == "May" or month == "October":
        total_price_studio *= 0.70
elif nights > 7:
    if month == "May" or month == "October":
        total_price_studio *= 0.95

print(f"Apartment: {total_price_apartment:.2f} lv.")
print(f"Studio: {total_price_studio:.2f} lv.")
