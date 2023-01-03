type = input()
rows = int(input())
cols = int(input())

total_seats = rows * cols
price_per_ticket = 0

if type == "Premiere":
    price_per_ticket = 12
elif type == "Normal":
    price_per_ticket = 7.50
elif type == "Discount":
    price_per_ticket = 5

total_price = price_per_ticket * total_seats

print(f"{total_price:.2f} leva")
