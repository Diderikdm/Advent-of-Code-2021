def find_route(start, target, steps, best):
    q = [(steps, start[0], start[1])]
    while q:
        q = [(steps,x,y) for steps,x,y in q if (x,y) not in best or best[(x,y)] > steps]
        steps, x, y = min(q)
        q.remove((steps, x, y))
        best[(x,y)] = steps
        if (x,y) == target:
            return best[(x,y)]
        for a, b in [coord for coord in ((x,y+1), (x-1,y), (x+1,y), (x,y-1)) if coord in grid]:
            q.append((steps + grid[(a,b)], a, b))             

with open("2021 day15.txt", 'r') as file:
    data = [[int(x) for x in y] for y in file.read().splitlines()]
    grid = {(x,y) : data[y][x] for x in range(len(data[0])) for y in range(len(data))}
    print(find_route((0,0), (len(data[0]) - 1, len(data) - 1), 0, {}))
    for z in [lambda: (x + i * len(data[0]), y), lambda: (x, y + i * len(data))]:
        new_coords = {}
        for x,y in grid:
            for i in range(1,5):
                new_coords[z()] = (grid[(x,y)] + i - 1) % 9 + 1
        grid.update(new_coords)
    print(find_route((0,0), (len(data[0]) * 5 - 1, len(data) * 5 - 1), 0, {}))
