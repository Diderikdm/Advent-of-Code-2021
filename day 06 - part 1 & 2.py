from collections import defaultdict

def calc(begin, end, data):
    for x in range(begin, end):
        temp = defaultdict(int)
        temp[6] = temp[8] = data[0]
        for y in range(1, 9):
            temp[y - 1] += data[y]  
        data = temp
    return data

with open("2021 day6.txt", 'r') as file:
    data = defaultdict(int)
    for x in file.read().split(','):
        data[int(x)] += 1   
    data = calc(0, 80, data)           
    print(sum(data.values()))
    print(sum(calc(80, 256, data).values()))
