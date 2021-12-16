from math import prod

def parse_bin(string, versions, values, origin, val = '', op = None):
    v, t, string = int(string[:3], 2), int(string[3:6], 2), string[6:]
    if t == 4:
        while op != '0':
            op, val, string = string[0], val + string[1:5], string[5:]
        return string, versions + [v], origin + [int(val, 2)]
    if string[0] == '0' and (length := lengths[string[0]](string)):
        copy, string = string[16 : 16 + length], string[16 + length:]
        while len(copy) > 5:
            copy, versions, values = parse_bin(copy, versions, [], values)
    else:
        string, length = string[12:], lengths[string[0]](string)
        for e in range(length):
            string, versions, values = parse_bin(string, versions, [], values)
    return string, versions + [v], origin + [types[t](*values)]

with open("2021 day16.txt", 'r') as file:
    data = [bin(int(raw, 16))[2:].zfill(len(raw) * 4) for raw in [file.read()]][0]
    lengths = {'0': lambda x: int(x[1:16], 2), '1': lambda x: int(x[1:12], 2)}
    types = {0:lambda *v:sum(v), 1:lambda *v:prod(v), 2:lambda *v:min(v), 3:lambda *v:max(v), 5:lambda x,y:int(x>y), 6:lambda x,y:int(x<y), 7:lambda x,y:int(x==y)}
    data, versions, values = parse_bin(data, [], [], [])
    print(sum(versions))
    print(values[0])
