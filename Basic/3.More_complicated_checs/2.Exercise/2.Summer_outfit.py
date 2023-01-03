degrees = int(input())
the_time = input()

outfit = ""
shoes = ""

if degrees <= 18:
    if the_time == "Morning":
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif the_time == "Afternoon":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif the_time == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
elif degrees <= 24:
    if the_time == "Morning":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif the_time == "Afternoon":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif the_time == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
elif degrees >= 25:
    if the_time == "Morning":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif the_time == "Afternoon":
        outfit = "Swim Suit"
        shoes = "Barefoot"
    elif the_time == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
