list = [1, 2, 3, 5, 8, 9, 56]


for idx, value in enumerate(list):
    if idx == 0:
        current_min = value
        current_max = value
    elif current_max < value:
        current_max = value
    elif current_min > value:
        current_min = value

print("Max: ", current_max)
print("Min: ", current_min)