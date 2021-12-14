from collections import defaultdict

with open("2021 day14.txt", 'r') as file:
    data, instructions = [x for x in file.read().split('\n\n')]
    start, end = data[0], data[-1]
    instructions = {x : [x[0] + y, y + x[1]] for x,y in [z.split(' -> ') for z in instructions.splitlines()]}
    amt_inst = {x : data.count(x) for x in instructions}
    for i in range(40):
        new_amt = defaultdict(int)
        for k,v in amt_inst.items():
            for x in instructions[k]:
                new_amt[x] += v
        amt_inst = new_amt
        if i in [9,39]:
            chars = defaultdict(int, {start : 1, end : 1})
            for k,v in amt_inst.items():
                for char in [chr(x) for x in range(65,91)]:
                    chars[char] += k.count(char) * v
            vals = [v // 2 for v in chars.values() if v]
            print(max(vals) - min(vals))
