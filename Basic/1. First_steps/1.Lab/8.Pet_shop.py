dog_food_price = 2.50
cat_food_price = 4

dog_food_count = int(input())
cat_food_count = int(input())

dog_expenses = dog_food_count * dog_food_price
cat_expenses = cat_food_count * cat_food_price

total_expenses = dog_expenses + cat_expenses

print(f"{total_expenses} lv.")
