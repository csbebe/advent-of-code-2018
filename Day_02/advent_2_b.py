file = open("advent_2_input.txt", "r").read().splitlines()

for x in file:
    for y in file:
        result = ""
        match = 0
        for position, char in enumerate(x):
            if char == y[position]:
                match += 1
                result += char
        if len(y) - match == 1:
            print(result)
