yearly_fee = int(input())
sneakers = yearly_fee * 0.60
shirt_pants = sneakers * 0.80
ball = shirt_pants / 4
accessories = ball / 5

total_expenses = yearly_fee + sneakers + shirt_pants + ball + accessories
print(total_expenses)
