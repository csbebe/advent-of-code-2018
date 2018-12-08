from collections import Counter

file = open("advent_2_input.txt", "r")

x, y = 0, 0
for line in file:
    list = Counter(Counter(line).values())
    if 2 in list:
        x += 1
    if 3 in list:
        y += 1
print(x * y)
