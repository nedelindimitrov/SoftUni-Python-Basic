age = int(input())

total_money = 0

money_birthday = 10

total_toys = 0

for n in range(1, age + 1):
    if n % 2 == 0:
        total_money += money_birthday
        money_birthday += 10
        total_money -= 1
    else:
        total_toys += 1

washing_machine_price = float(input())

price_per_toy = int(input())

total_money += (total_toys * price_per_toy)

if total_money >= washing_machine_price:
    print(f"Yes! {total_money - washing_machine_price:.2f}")
else:
    print(f"No! {washing_machine_price - total_money:.2f}")
