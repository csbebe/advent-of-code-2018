import itertools

file = open("advent_1_input.txt", "r")
result = 0
seen = {0}
for line in itertools.cycle(file):
    result += int(line)
    if result in seen:
        print(result)
        break
    seen.add(result)
