total_money = 0

while True:
    deposit = input()
    if deposit == "NoMoreMoney":
        print(f"Total: {total_money:.2f}")
        break
    else:
        deposit = float(deposit)
    if deposit <= 0:
        print("Invalid operation!")
        print(f"Total: {total_money:.2f}")
        break

    total_money += deposit
    print(f"Increase: {deposit:.2f}")
