first_side = int(input())
second_side = int(input())

total_pieces = first_side * second_side

while True:
    command = input()
    if command == "STOP":
        print(f"{total_pieces} pieces are left.")
        break
    pieces_ate = int(command)
    total_pieces -= pieces_ate
    if total_pieces <= 0:
        print(f"No more cake left! You need {abs(total_pieces)} pieces more.")
        break
