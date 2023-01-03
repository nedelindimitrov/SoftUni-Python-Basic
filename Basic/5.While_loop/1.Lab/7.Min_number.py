min_number = int(input())

while True:
    current = input()
    if current == "Stop":
        print(min_number)
        break
    this_num = int(current)
    if this_num < min_number:
        min_number = this_num
