x_or_y = lambda x,y : x if 'x' in instruction else y
new_coord = lambda: (inst + (inst - x), y) if 'x' in instruction else (x, inst + (inst - y))

with open("2021 day13.txt", 'r') as file: 
    data, folds = [x.splitlines() for x in file.read().split('\n\n')]
    grid = {tuple(int(z) for z in y.split(',')) : '#' for y in data}
    for e, instruction in enumerate(folds):
        inst = int(instruction.split('=')[-1])
        to_fold = [(x,y) for x,y in grid if x_or_y(x,y) > inst]
        for x,y in to_fold:
            grid[new_coord()] = grid.pop((x,y))
        if e == 0:
            print(len(grid))
    print('\n'.join([''.join([' ' if (x,y) not in grid else grid[(x,y)] for x in range(max(x[0] for x in grid)+1)]) for y in range(max(x[1] for x in grid)+1)]))
