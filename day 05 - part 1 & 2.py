from collections import defaultdict

with open("2021 day5.txt", 'r') as file: 
    data = [[[int(z) for z in y.split(',')] for y in x.split(' -> ')] for x in file.read().splitlines()]
    grid = defaultdict(int)
    for first, second in filter(lambda x: x[0][0] == x[1][0] or x[0][1] == x[1][1], data):
        for x in range(min(first[0], second[0]), max(first[0], second[0]) + 1):
            for y in range(min(first[1], second[1]), max(first[1], second[1]) + 1):
                grid[(x,y)] += 1
    print(sum(1 for v in grid.values() if v >= 2))
    
    for first, second in filter(lambda x: x[0][0] != x[1][0] and x[0][1] != x[1][1], data):
        start, end = sorted([first, second], key = lambda x: x[0])
        vect = 1 if start[1] < end[1] else -1
        y = start[1]
        for x in range(start[0], end[0] + 1):
            grid[(x,y)] += 1
            y += vect
    print(sum(1 for v in grid.values() if v >= 2))
