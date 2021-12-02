with open("2021 day2.txt", 'r') as file:
    data = [x.split() for x in file.read().splitlines()]
    aim, x1, y1, x2, y2 = 0, 0, 0, 0, 0
    move = {'forward' : lambda aim, x1, y1, x2, y2, z : (aim, x1 + z, y1, x2 + z, y2 + (z * aim)),
            'down'    : lambda aim, x1, y1, x2, y2, z : (aim + z, x1, y1 + z, x2, y2),
            'up'      : lambda aim, x1, y1, x2, y2, z : (aim - z, x1, y1 - z, x2, y2)}
    for instruction, amt in data:
        aim, x1, y1, x2, y2 = move[instruction](aim, x1, y1, x2, y2, int(amt))
    print(x1 * y1)
    print(x2 * y2)
