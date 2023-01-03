puzzle_price = 2.60
talking_doll_price = 3
bear_price = 4.10
minion_price = 8.20
truck_price = 2

money_needed = float(input())

puzzle_amount = int(input())
talking_doll_amount = int(input())
bear_amount = int(input())
minion_amount = int(input())
truck_amount = int(input())

total_amount = puzzle_amount + talking_doll_amount + bear_amount + minion_amount + truck_amount
first_profit = puzzle_amount * puzzle_price + talking_doll_amount * talking_doll_price + bear_amount * bear_price + \
    minion_amount * minion_price + truck_amount * truck_price

if total_amount >= 50:
    first_profit *= 0.75

final_profit = first_profit * 0.90

if final_profit >= money_needed:
    print(f"Yes! {final_profit - money_needed:.2f} lv left.")
else:
    print(f"Not enough money! {money_needed - final_profit:.2f} lv needed.")
