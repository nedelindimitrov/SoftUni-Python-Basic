chicken_menu = 10.35
fish_menu = 12.40
vegetarian_menu = 8.15

chicken_order = int(input())
fish_order = int(input())
vegetarian_order = int(input())

first_total_order = chicken_order * chicken_menu + fish_order * fish_menu + vegetarian_order * vegetarian_menu
dessert = first_total_order * 0.20
delivery = 2.50

final_total_order = first_total_order + dessert + delivery
print(f"{final_total_order:.2f}")
