tabs_open = int(input())

salary = int(input())

not_lost = True

for n in range(tabs_open):
    current_website = input()
    if current_website == "Facebook":
        salary -= 150
    elif current_website == "Instagram":
        salary -= 100
    elif current_website == "Reddit":
        salary -= 50

    if salary <= 0:
        print("You have lost your salary.")
        not_lost = False
        break

if not_lost:
    print(salary)
