days = int(input())
nights = days - 1
room_type = input()
p_or_n = input()

price_per_night = 0

if room_type == "room for one person":
    price_per_night = 18
elif room_type == "apartment":
    price_per_night = 25
elif room_type == "president apartment":
    price_per_night = 35

total = nights * price_per_night

if room_type == "room for one person":
    pass
elif room_type == "apartment":
    if nights < 10:
        total *= 0.70
    elif nights <= 15:
        total *= 0.65
    else:
        total *= 0.50
elif room_type == "president apartment":
    if nights < 10:
        total *= 0.90
    elif nights <= 15:
        total *= 0.85
    else:
        total *= 0.80

if p_or_n == "positive":
    total *= 1.25
elif p_or_n == "negative":
    total *= 0.90

print(f"{total:.2f}")
