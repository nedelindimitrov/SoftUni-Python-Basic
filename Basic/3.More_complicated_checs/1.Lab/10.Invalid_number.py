number = int(input())

is_valid = False

if number >= 100 and number <= 200:
    is_valid = True

if number == 0:
    is_valid = True

if not is_valid:
    print("invalid")
