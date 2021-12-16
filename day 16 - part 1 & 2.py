from functools import reduce

def append(v, lst):
    if type(v) == list:
        for x in v:
            lst.append(x)
    else:
        lst.append(v)
        
def parse_bin(string, values, val = '', i = 0):
    v, t, string = int(string[:3], 2), int(string[3:6], 2), string[6:]
    versions.append(v)
    if t == 4:
        while True:
            op, i = string[0], i + 5
            val += string[1:5]
            string = string[5:]
            if op == '0':
                return string, values + [int(val, 2)]
    else:
        length = lengths[string[0]](string)
        if string[0] == '0':
            copy = string[16 : 16 + length]
            while len(copy) > 5:
                copy, v = parse_bin(copy, [])
                append(v, values)
            string = string[16 + length:]
        else:
            string = string[12:]
            for e in range(length):
                string, v = parse_bin(string, [])
                append(v, values)
    return string, types[t](values)
    
with open("2021 day16.txt", 'r') as file:
    raw = file.read()
    data = bin(int(raw, 16))[2:].zfill(len(raw) * 4)
    versions, values, outer_type = [], [], int(data[3:6], 2)
    lengths = {'0': lambda x: int(x[1:16], 2), '1': lambda x: int(x[1:12], 2)}
    types = {0:lambda values:sum(values),
             1:lambda values:reduce(lambda x,y: x*y, values),
             2:lambda values:min(values),
             3:lambda values:max(values),
             5:lambda values:int(values[0] > values[1]),
             6:lambda values:int(values[0] < values[1]),
             7:lambda values:int(values[0] == values[1])}
    while len(data) > 11:
        data, values = parse_bin(data, [])
    print(sum(versions))
    print(values)
