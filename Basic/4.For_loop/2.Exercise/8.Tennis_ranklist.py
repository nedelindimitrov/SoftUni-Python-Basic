all_tours = int(input())
points = int(input())

tours_won = 0
points_won = 0

for _ in range(all_tours):
    current = input()
    if current == "W":
        tours_won += 1
        points += 2000
        points_won += 2000
    elif current == "F":
        points += 1200
        points_won += 1200
    elif current == "SF":
        points += 720
        points_won += 720

estimated_points_won = int(points_won / all_tours)
percent_won = tours_won / all_tours * 100

print(f"Final points: {points}")
print(f"Average points: {estimated_points_won}")
print(f"{percent_won:.2f}%")
