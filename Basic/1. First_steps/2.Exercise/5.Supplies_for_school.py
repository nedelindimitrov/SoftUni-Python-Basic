pen_price = 5.80
markers_price = 7.20
chemical_price = 1.20

pen_count = int(input())
markers_count = int(input())
chemical_count = int(input())
discount_percent = int(input())

discount_for_calculator = discount_percent / 100

pen_sum = pen_count * pen_price
markers_sum = markers_count * markers_price
chemical_sum = chemical_count * chemical_price

total_sum_without_discount = pen_sum + markers_sum + chemical_sum
discount = total_sum_without_discount * discount_for_calculator

total_sum = total_sum_without_discount - discount
print(total_sum)
