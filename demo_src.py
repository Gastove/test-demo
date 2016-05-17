"""
This is a tic-tac-toe victory checker. It looks at a tic-tac-toe board,
represented by an array of arrays, and determines if x won, y won, or the board
is a draw.
"""


def row_status(row):
    s = set(row)
    if len(s) == 1:
        return row[0]
    else:
        return "no winner"


def check_for_winner(parsed_game):
    result = [row_status(row) for row in parsed_game]
    if "x" in result:
        return "x"
    if "o" in result:
        return "o"
    else:
        return "draw"


def parse_aoa_to_array(aoa):
    parsed = [] + aoa

    diagonal_one = []
    diagonal_two = []

    for i in range(3):
        column = [aoa[0][i], aoa[1][i], aoa[2][i]]
        parsed.append(column)

        diagonal_one.append(aoa[i][i])
        diagonal_two.append(aoa[2 - i][2 - i])

    parsed.append(diagonal_one)
    parsed.append(diagonal_two)

    return parsed


def validate(aoa):
    return aoa


def check(game):
    validate(game)
    parsed_game = parse_aoa_to_array(game)
    return check_for_winner(parsed_game)
