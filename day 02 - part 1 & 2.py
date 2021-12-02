with open("2021 day2.txt", 'r') as file:
    data = [x.split() for x in file.read().splitlines()]
    aim, x1, y1, x2, y2 = 0, 0, 0, 0, 0
    move = {
        'forward' : lambda aim, x, y, z, part : (aim, x + z, y) if part == 1 else (aim, x + z, y + (z * aim)),
        'down'    : lambda aim, x, y, z, part : (aim, x, y + z) if part == 1 else (aim + z, x, y),
        'up'      : lambda aim, x, y, z, part : (aim, x, y - z) if part == 1 else (aim - z, x, y)
        }
    for instruction, amt in data:
        aim, x1, y1 = move[instruction](aim, x1, y1, int(amt), 1)
        aim, x2, y2 = move[instruction](aim, x2, y2, int(amt), 2)
    print(x1 * y1)
    print(x2 * y2)
