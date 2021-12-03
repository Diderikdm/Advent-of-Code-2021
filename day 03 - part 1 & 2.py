with open("2021 day3.txt", 'r') as file:
    data = file.read().splitlines()
    verticals = [[y[x] for y in data] for x in range(len(data[0]))]
    gamma, epsilon, oxy, co2 = [], [], data[:], data[:]
    for i,x in enumerate(verticals):
        most = 0 if x.count('0') > x.count('1') else 1
        gamma.append(most)
        epsilon.append(int(not(most)))
        if len(oxy) > 1:
            current_oxy = [[y[z] for y in oxy] for z in range(len(oxy[0]))]
            oxy = [x for x in oxy if int(x[i]) == (0 if current_oxy[i].count('0') > current_oxy[i].count('1') else 1)]
        if len(co2) > 1:
            current_co2 = [[y[z] for y in co2] for z in range(len(co2[0]))]
            co2 = [x for x in co2 if int(x[i]) == (1 if current_co2[i].count('0') > current_co2[i].count('1') else 0)]    
    print(int(''.join([str(x) for x in gamma]), 2) * int(''.join([str(x) for x in epsilon]), 2))
    print(int(''.join([str(x) for x in oxy]), 2) * int(''.join([str(x) for x in co2]), 2))
