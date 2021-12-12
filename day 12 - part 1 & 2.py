from collections import defaultdict

def find_routes(current, path, p2=False):
    if current == 'end':
        routes.add(tuple(path))
        return
    for x in data[current]:
        if (x.islower() and x in path and not p2) \
        or (x.islower() and x in path and any(path.count(y) > 1 for y in path if y.islower()) and p2 or x == 'start'):
            continue
        find_routes(x, path + [x], p2)
    return len(routes)
        
with open("2021 day12.txt", 'r') as file:
    data = defaultdict(list)
    for x in file.read().splitlines():
        a,b = x.split('-')
        data[a] += [b]
        data[b] += [a]
    routes = set()
    print(find_routes('start', ['start']))
    print(find_routes('start', ['start'], True))
