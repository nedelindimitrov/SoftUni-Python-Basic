hour = int(input())
day = input()

if day == "Sunday" or hour < 10 or hour > 18:
    print("closed")
else:
    print("open")
