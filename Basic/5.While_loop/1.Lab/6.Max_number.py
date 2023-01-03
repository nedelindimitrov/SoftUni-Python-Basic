max_number = int(input())

while True:
    current = input()
    if current == "Stop":
        print(max_number)
        break
    this_num = int(current)
    if this_num > max_number:
        max_number = this_num
