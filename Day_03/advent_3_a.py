file = open("advent_3_input.txt", "r").read().splitlines()

def process(line):
    claim = line.split(' ')
    pos_x = int(claim[2].split(',')[0])
    pos_y = int(claim[2].split(',')[1].replace(":", ""))
    width = int(claim[3].split('x')[0])
    height = int(claim[3].split('x')[1])
    return pos_x, pos_y, width, height

fabric = dict()
value = 0
for line in file:
    x, y, w, h = process(line)
    for i in range(x, x + w):
        for j in range(y, y + h):
            fabric[(i, j)] = fabric[(i, j)] + 1 if (i, j) in fabric else 1

overlap_cntr = 0
for v in fabric.values():
    if v >= 2:
        overlap_cntr += 1

print(overlap_cntr)
