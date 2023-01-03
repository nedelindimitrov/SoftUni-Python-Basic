levels = int(input())
rooms = int(input())
symbol = " "
for vertical in range(levels, 0 , -1):
    for horizontal in range(rooms):
        if vertical == levels:
            symbol = "L"
        elif vertical % 2 == 0:
            symbol = "O"
        elif vertical % 2 == 1:
            symbol = "A"
        print(f"{symbol}{vertical}{horizontal}", end= " ")
    print()
