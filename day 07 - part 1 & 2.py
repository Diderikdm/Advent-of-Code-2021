with open("2021 day7.txt", 'r') as file:
    data = [int(x) for x in file.read().split(',')]
    print(min(sum(abs(i - x) for x in data) for i in range(min(data), max(data) + 1)))
    print(min(sum(sum(range(abs(i - x) + 1)) for x in data) for i in range(min(data), max(data) + 1))) 
