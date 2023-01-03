city = input()
sales_amount = float(input())

true_boolean = True

city_list = ["Sofia", "Varna", "Plovdiv"]

if city not in city_list:
    true_boolean = False

if sales_amount < 0:
    true_boolean = False


trade_percent = 0

if true_boolean:
    if city == "Sofia":
        if sales_amount <= 500:
            trade_percent = 0.05
        elif sales_amount <= 1000:
            trade_percent = 0.07
        elif sales_amount <= 10000:
            trade_percent = 0.08
        elif sales_amount > 10000:
            trade_percent = 0.12
    elif city == "Varna":
        if sales_amount <= 500:
            trade_percent = 0.045
        elif sales_amount <= 1000:
            trade_percent = 0.075
        elif sales_amount <= 10000:
            trade_percent = 0.10
        elif sales_amount > 10000:
            trade_percent = 0.13
    elif city == "Plovdiv":
        if sales_amount <= 500:
            trade_percent = 0.055
        elif sales_amount <= 1000:
            trade_percent = 0.08
        elif sales_amount <= 10000:
            trade_percent = 0.12
        elif sales_amount > 10000:
            trade_percent = 0.145
    final_answer = sales_amount * trade_percent
    print(f"{final_answer:.2f}")
else:
    print("error")
