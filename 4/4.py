input_file = open('input.txt', 'r')

numbers = (i for i in input_file.readline().split(','))
input_file.readline()


def make_board(it):
    return [
        [i for i in row.split(' ') if i != ''] for row in it
    ]


lines = list(l for l in input_file.read().splitlines() if l != '')
boards = [
    make_board(lines[i:i + 5]) for i in range(0, len(lines), 5)  # lineas tomadas en grupos de a 5
]


def mark_number(board, number):
    return [
        [i if i != number else 0 for i in line]
        for line in board
    ]


def check_board(board):
    total = 0
    winner = False
    for i in range(5):
        row = True
        column = True
        for j in range(5):
            total += int(board[i][j])
            row = row and not bool(board[i][j])
            column = column and not bool(board[j][i])
        winner = winner or row or column
    return total if winner else 0


winner_total = 0
for number in numbers:
    boards = [mark_number(board, number) for board in boards]
    winner_total = next((n for n in (check_board(board) for board in boards) if n != 0), 0) * int(number)
    if winner_total > 0:
        break

print(winner_total)
