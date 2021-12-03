def get_vertical(lst):
    return [[y[x] for y in lst] for x in range(len(lst[0]))]

with open("2021 day3.txt", 'r') as file:
    data = file.read().splitlines()
    verticals = get_vertical(data)
    gamma, epsilon, oxy, co2 = [], [], data[:], data[:]
    for i,x in enumerate(verticals):
        most = 0 if x.count('0') > x.count('1') else 1
        gamma.append(most)
        epsilon.append(int(not(most)))
        if len(oxy) > 1:
            current_oxy = get_vertical(oxy)
            oxy = [x for x in oxy if int(x[i]) == (0 if current_oxy[i].count('0') > current_oxy[i].count('1') else 1)]
        if len(co2) > 1:
            current_co2 = get_vertical(co2)
            co2 = [x for x in co2 if int(x[i]) == (1 if current_co2[i].count('0') > current_co2[i].count('1') else 0)]    
    print(int(''.join([str(x) for x in gamma]), 2) * int(''.join([str(x) for x in epsilon]), 2))
    print(int(''.join([str(x) for x in oxy]), 2) * int(''.join([str(x) for x in co2]), 2))
   
