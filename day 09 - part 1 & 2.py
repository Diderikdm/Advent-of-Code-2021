from functools import reduce

def find_basin(key, current):
    for k in adj(*key):
        if k not in prev and grid[k] != 9:
            prev.add(k)
            current = find_basin(k, current + [k])
    return current
            
with open("2021 day9.txt", 'r') as file:
    data = [[int(y) for y in x] for x in file.read().splitlines()]
    grid = {(x,y) : data[y][x] for x in range(len(data[0])) for y in range(len(data))}
    adj = lambda x,y: [z for z in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)] if z in grid]
    print(sum(1 + grid[k] for k in grid if all(grid[x] > grid[k] for x in adj(*k))))
    prev = set()
    basins = []
    for k,v in grid.items():
        if k not in prev and v != 9:
            prev.add(k)
            basins.append(len(find_basin(k, [k])))
    print(reduce((lambda x, y: x * y), sorted(basins, key = lambda x: -x)[:3]))
