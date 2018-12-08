file = open("advent_3_input.txt", "r").read().splitlines()

def process(line):
    claim = line.split(' ')
    id = int(claim[0].replace("#", ""))
    pos_x = int(claim[2].split(',')[0])
    pos_y = int(claim[2].split(',')[1].replace(":", ""))
    width = int(claim[3].split('x')[0])
    height = int(claim[3].split('x')[1])
    return id, pos_x, pos_y, width, height

fabric = dict()
all_claims = set()
value = 0
for line in file:
    id, x, y, w, h = process(line)
    all_claims.add(id)
    for i in range(x, x + w):
        for j in range(y, y + h):
            if (i, j) in fabric:
                fabric[(i, j)].add(id)
            else:
                fabric[(i, j)] = {id}

bad_claims = set()
for v in fabric.values():
    if len(v) >= 2:
        bad_claims.update(v)

print(all_claims.difference(bad_claims))
