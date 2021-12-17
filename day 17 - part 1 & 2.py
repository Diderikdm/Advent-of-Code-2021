with open("2021 day17.txt", 'r') as file:
    minx, maxx, miny, maxy = sum([[int(y) for y in x.split('=')[1].split('..')] for x in file.read().split(', ')], [])
    count, best = 0, 0
    for tx in range(1, maxx + 1):
        for ty in range(miny, -maxy + (maxy - miny)):
            x, y, h = 0, 0, 0
            vx, vy = tx, ty
            while vx > 0 or y > miny:
                x, y, h = x + vx, y + vy, max(h,y)
                vx, vy = max(0, vx - 1), vy - 1
                if minx <= x <= maxx and miny <= y <= maxy:
                    count += 1
                    best = max(best, h)
                    break
    print(best)
    print(count)
