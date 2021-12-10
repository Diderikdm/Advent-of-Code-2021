def find_syntax(row, score=0):
    while row:
        i = next((e for e, x in enumerate(row) if x in scores), None)
            if i:
                if syntax[row[i-1]] == row[i]:
                    row = row[:i-1] + row[i+1:]
                    continue
                return scores[row[i]][0]

        for x in row[::-1]:
            score = score * 5 + scores[syntax[x]][1]
        p2_scores.append(score)

        return 0

with open("2021 day10.txt", 'r') as file:
    data = file.read().splitlines()
    syntax = {'<' : '>', '(' : ')', '[' : ']', '{' : '}'}
    scores = {')' : [3, 1], ']' : [57, 2], '}' : [1197, 3], '>' : [25137, 4]}
    score = 0
    p2_scores = []
    for row in data:
        score += find_syntax(row)
    print(score)
    print(sorted(p2_scores)[(len(p2_scores) - 1) // 2])
