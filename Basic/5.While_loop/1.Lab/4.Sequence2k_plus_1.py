input_number = int(input())

current = 1

while True:
    print(current)
    current = current * 2 + 1
    if current > input_number:
        break
