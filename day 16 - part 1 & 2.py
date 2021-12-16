from math import prod

def parse_bin(string, values, origin, versions, val = '', op = None):
    v, t, string = int(string[:3], 2), int(string[3:6], 2), string[6:]
    if t == 4:
        while op != '0':
            op, val, string = string[0], val + string[1:5], string[5:]
        return string, origin + [int(val, 2)], versions + [v]
    length = lengths[string[0]](string)
    if string[0] == '0':
        copy, string = string[16 : 16 + length], string[16 + length:]
        while len(copy) > 5:
            copy, values, versions = parse_bin(copy, [], values, versions)
    else:
        string = string[12:]
        for e in range(length):
            string, values, versions = parse_bin(string, [], values, versions)
    return string, origin + [types[t](*values)], versions + [v]

with open("2021 day16.txt", 'r') as file:
    data = [bin(int(raw, 16))[2:].zfill(len(raw) * 4) for raw in [file.read()]][0]
    lengths = {'0': lambda x: int(x[1:16], 2), '1': lambda x: int(x[1:12], 2)}
    types = {0:lambda *v:sum(v), 1:lambda *v:prod(v), 2:lambda *v:min(v), 3:lambda *v:max(v), 5:lambda x,y:int(x>y), 6:lambda x,y:int(x<y), 7:lambda x,y:int(x==y)}
    data, values, versions = parse_bin(data, [], [], [])
    print(sum(versions))
    print(values[0])
