price_per_one = 7.61
meters_for_greening = float(input())
price_without_discount = meters_for_greening * price_per_one
discount = price_without_discount * 0.18
total_price = price_without_discount - discount

print(f"The final price is: {total_price} lv.")
print(f"The discount is: {discount} lv.")
