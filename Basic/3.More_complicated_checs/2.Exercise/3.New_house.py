price_per_unit = 0

flower = input()
units_count = int(input())
budget = int(input())

if flower == "Roses":
    price_per_unit = 5
elif flower == "Dahlias":
    price_per_unit = 3.80
elif flower == "Tulips":
    price_per_unit = 2.80
elif flower == "Narcissus":
    price_per_unit = 3
elif flower == "Gladiolus":
    price_per_unit = 2.50

needed_money = units_count * price_per_unit

if flower == "Roses":
    if units_count > 80:
        needed_money *= 0.90
elif flower == "Dahlias":
    if units_count > 90:
        needed_money *= 0.85
elif flower == "Tulips":
    if units_count > 80:
        needed_money *= 0.85
elif flower == "Narcissus":
    if units_count < 120:
        needed_money *= 1.15
elif flower == "Gladiolus":
    if units_count < 80:
        needed_money *= 1.20

if budget >= needed_money:
    print(f"Hey, you have a great garden with {units_count} {flower} and {budget - needed_money:.2f} leva left.")
else:
    print(f"Not enough money, you need {needed_money - budget:.2f} leva more.")
