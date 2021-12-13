with open("2021 day13.txt", 'r') as file:
    data, folds = [x.splitlines() for x in file.read().split('\n\n')]
    grid = {tuple(int(z) for z in y.split(',')) : '#' for y in data}
    for e, instruction in enumerate(folds):
        inst = int(instruction.split()[-1].split('=')[-1])
        to_fold = [x for x in grid.keys() if x[0 if 'x' in instruction else 1] > inst]
        for k in to_fold:
            grid[(inst + (inst - k[0]), k[1]) if 'x' in instruction else (k[0], inst + (inst - k[1]))] = grid.pop(k)
        if e == 0:
            print(len(grid))
    print('\n'.join([''.join([' ' if (x,y) not in grid else grid[(x,y)] for x in range(max(x[0] for x in grid.keys())+1)]) for y in range(max(x[1] for x in grid.keys())+1)]))
