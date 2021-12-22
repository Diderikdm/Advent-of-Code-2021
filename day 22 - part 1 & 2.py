def solve(minx, maxx, miny, maxy, minz, maxz, c):
    cubes = set(c)
    for mina, maxa, minb, maxb, minc, maxc in c:
        min_int_x, max_int_x = max(minx, mina), min(maxx, maxa)
        min_int_y, max_int_y = max(miny, minb), min(maxy, maxb)
        min_int_z, max_int_z = max(minz, minc), min(maxz, maxc)
        if min_int_x <= max_int_x and min_int_y <= max_int_y and min_int_z <= max_int_z:
            cubes.discard((mina, maxa, minb, maxb, minc, maxc))
            if mina <= min_int_x <= maxa:
                cubes.add((mina, min_int_x - 1, minb, maxb, minc, maxc))
                mina = min_int_x
            if mina <= max_int_x <= maxa:
                cubes.add((max_int_x + 1, maxa, minb, maxb, minc, maxc))
                maxa = max_int_x
            if minb <= min_int_y <= maxb:
                cubes.add((mina, maxa, minb, min_int_y - 1, minc, maxc))
                minb = min_int_y
            if minb <= max_int_y <= maxb:
                cubes.add((mina, maxa, max_int_y + 1, maxb, minc, maxc))
                maxb = max_int_y
            if minc <= min_int_z <= maxc:
                cubes.add((mina, maxa, minb, maxb, minc, min_int_z - 1))
                minc = min_int_z
            if minc <= max_int_z <= maxc:
                cubes.add((mina, maxa, minb, maxb, max_int_z + 1, maxc))
                maxc = max_int_z
    return cubes
        
with open("2021 day22.txt", 'r') as file:
    data = file.read().splitlines()
    cubes = set()
    p1 = None
    for row in data:
        op, coords = row.split()
        minx, maxx, miny, maxy, minz, maxz = sum([[int(i) for i in e.split('=')[1].split('..')] for e in coords.split(',')], [])
        if all(-50 <= mina and maxa <= 50 for mina, maxa in [[minx, maxx], [miny, maxy], [minz, maxz]]):
            if not cubes:
                cubes.add((minx, maxx, miny, maxy, minz, maxz))
            else:
                cubes = solve(minx, maxx, miny, maxy, minz, maxz, cubes)
                if op == 'on':
                    cubes.add((minx, maxx, miny, maxy, minz, maxz))
        else:
            if not p1:
                p1 = sum((maxx + 1 - minx) * (maxy + 1 - miny) * (maxz + 1 - minz) for minx, maxx, miny, maxy, minz, maxz in cubes)
                print(p1)
            cubes = solve(minx, maxx, miny, maxy, minz, maxz, cubes)
            if op == 'on':
                cubes.add((minx, maxx, miny, maxy, minz, maxz))                         
    print(sum((maxx + 1 - minx) * (maxy + 1 - miny) * (maxz + 1 - minz) for minx, maxx, miny, maxy, minz, maxz in cubes))
