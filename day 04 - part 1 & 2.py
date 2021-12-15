get_vertical = lambda board: [[y[x] for y in board] for x in range(len(board[0]))]
get_unmarked = lambda board: [x for x in sum([list(y) for y in board], []) if x not in play]

with open("2021 day4.txt", 'r') as file: 
    data = file.read().split('\n\n')
    numbers = [int(x) for x in data[0].split(',')]
    boards, play, rows, found_numbers, board_values, used_rows, used_boards = {}, [], [], [], [], [], [] 
    for e,x in enumerate(data[1:]):
        board = [[int(y) for y in row.split()] for row in x.splitlines()]
        vert_board = get_vertical(board)
        boards[e] = [tuple(sorted(x)) for x in board + vert_board]
    all_rows = sum(boards.values(), [])
    while len(used_boards) < len(boards):
        number = numbers.pop(0)
        play = tuple(sorted([x for x in play] + [number]))
        found_rows = [row for row in all_rows if all(x in play for x in row) and row not in used_rows]
        for row in found_rows:
            for key, board in boards.items():
                if row in board and key not in used_boards:
                    used_boards.append(key)
                    used_rows.append(row)
                    board_values.append(sum(set(get_unmarked(board))) * number)                     
    print(board_values[0])
    print(board_values[-1])
