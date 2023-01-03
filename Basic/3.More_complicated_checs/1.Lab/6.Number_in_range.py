number = int(input())

is_it = True

if number < -100 or number > 100 or number == 0:
    is_it = False

if is_it:
    print("Yes")
else:
    print("No")
