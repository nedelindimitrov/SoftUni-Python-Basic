first_side = int(input())
second_side = int(input())
third_side = int(input())

total_space = first_side * second_side * third_side

while True:
    command = input()
    if command == "Done":
        print(f"{total_space} Cubic meters left.")
        break
    current_space = int(command)
    total_space -= current_space
    if total_space <= 0:
        print(f"No more free space! You need {abs(total_space)} Cubic meters more.")
        break
