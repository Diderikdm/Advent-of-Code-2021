from collections import defaultdict

def turn_current_and_append_to_grid(current):
    orientations = [possibles(*x) for x in current]
    for e in range(len(orientations[0])):
        current_orientation = [x[e] for x in orientations]
        current_distances, current_xyz_shifts = get_relative_beacon_distance(current_orientation, defaultdict(list), defaultdict(list))
        matches = {}
        for k,v in current_xyz_shifts.items():
            for ok, ov in grid_xyz_shifts.items():
                distance_matches = [x for x in v if x in ov]
                if len(distance_matches) >= 11:
                    matches[k] = ok
        if len(matches) >= 12:
            xyz_diff = next((tuple(v[i] - k[i] for i in range(3)) for k,v in matches.items()))
            for k in current_orientation:
               grid.add(tuple(k[i] + xyz_diff[i] for i in range(3)))
            point = next((k for k,v in matches.items()))
            scanners.append(tuple(matches[point][i] - point[i] for i in range(3)))
            return True
                    
def get_relative_beacon_distance(beacons, relative_distances, relative_xyz_shift):
    for coords in beacons:
        for other_coords in beacons:
            if coords != other_coords:
                relative_distances[coords].append(sum([(coords[e] - other_coords[e]) ** 2 for e in range(3)]))
                relative_xyz_shift[coords].append(tuple(other_coords[x] - coords[x] for x in range(3)))
    return relative_distances, relative_xyz_shift

with open("2021 day19.txt", 'r') as file:
    data = {e: [tuple(int(z) for z in y.split(',')) for y in x.splitlines()[1:]] for e,x in enumerate(file.read().split('\n\n'))}
    possibles = lambda x,y,z: [(x,y,z),(x,z,-y),(x,-y,-z),(x,-z,y),(-x,y,-z),(-x,z,y),(-x,-y,z),(-x,-z,-y),
                               (y,x,-z),(y,z,x),(y,-x,z),(y,-z,-x),(-y,x,z),(-y,z,-x),(-y,-x,-z),(-y,-z,x),
                               (z,x,y),(z,y,-x),(z,-x,-y),(z,-y,x),(-z,x,-y),(-z,y,x),(-z,-x,y),(-z,-y,-x)]
    mapped = [0]
    scanners = [(0,0,0)]
    grid = set(data.pop(0))
    grid_distances, grid_xyz_shifts = get_relative_beacon_distance(grid, defaultdict(list), defaultdict(list))
    while data:
        for key, current in data.items():
            current_distances, current_xyz_shifts = get_relative_beacon_distance(current, defaultdict(list), defaultdict(list))
            if any(any(len([distance for distance in current_distance if distance in grid_distance]) >= 11 for grid_distance in grid_distances.values()) for current_distance in current_distances.values()):
                success = turn_current_and_append_to_grid(current)
                if success:
                    mapped.append(key)
                    grid_distances, grid_xyz_shifts = get_relative_beacon_distance(grid, defaultdict(list), defaultdict(list))
                    data.pop(key)
                    break
    print(len(grid))
    print(max(sum([abs(x[i] - y[i]) for i in range(3)]) for x in scanners for y in scanners))
