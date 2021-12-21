def play_dirac_by_swap(current_player, other_player, current_score = 0, other_score = 0):
    if other_score >= 21:
        return 0, 1
    wins_current, wins_other = 0, 0
    for turn, times in odds_of_rolling_results:
        current_position = (current_player + turn - 1) % 10 + 1
        loss, win = play_dirac_by_swap(other_player, current_position, other_score, current_score + current_position)
        wins_current, wins_other = wins_current + times * win, wins_other + times * loss
    return wins_current, wins_other

with open("2021 day21.txt", 'r') as file:
    data = [int(x.split()[-1]) for x in file.read().splitlines()]
    players = {e : [x, 0] for e,x in enumerate(data)}
    dice, rolls, e = 0, 0, 0
    while not any(x[1] >= 1000 for x in players.values()):
        turn = 0
        for i in range(3):
            dice = (dice + 1) % 100
            turn += dice
            rolls += 1
        next_field = (players[e % 2][0] + turn - 1) % 10 + 1
        players[e % 2][0] = next_field
        players[e % 2][1] += next_field
        e += 1
    print(min(x[1] for x in players.values()) * rolls)
    odds_of_rolling_results = ((3,1), (4,3), (5,6), (6,7), (7,6), (8,3), (9,1))
    print(max(play_dirac_by_swap(*data))) 
