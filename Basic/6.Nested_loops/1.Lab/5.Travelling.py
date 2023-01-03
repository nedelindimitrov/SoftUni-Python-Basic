command0 = input()
while command0 != "End":
    destination = command0
    money_amount = 0
    needed_money = float(input())
    while True:
        money_add = float(input())
        money_amount += money_add
        if money_amount < needed_money:
            continue
        else:
            print(f"Going to {destination}!")
            command0 = input()
            break
