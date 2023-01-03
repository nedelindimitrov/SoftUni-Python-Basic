length = int(input())
width = int(input())
height = int(input())
percent = float(input())

tank_volume = length * width * height
volume_in_liters = tank_volume / 1000
reserved_part = percent / 100
needed_liters = volume_in_liters * (1 - reserved_part)

print(needed_liters)
