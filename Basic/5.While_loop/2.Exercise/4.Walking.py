step_goal = 10000

total_steps = 0

while True:
    current = input()
    if current == "Going home":
        another_step = int(input())
        total_steps += another_step
        if total_steps >= step_goal:
            print("Goal reached! Good job!")
            print(f"{total_steps - step_goal} steps over the goal!")
            break
        else:
            print(f"{step_goal - total_steps} more steps to reach goal.")
            break
    steps = int(current)
    total_steps += steps
    if total_steps >= step_goal:
        print("Goal reached! Good job!")
        print(f"{total_steps - step_goal} steps over the goal!")
        break
