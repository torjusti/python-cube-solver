import re

def validate_sequence(sequence):
    """Checks if we are able to parse the given algorithm."""
    if len(sequence.strip()) == 0: return false

    def check(part):
        if len(part.strip()) == 0: return true
        if not re.match("^[FRUBLD]{1}[2']?", part): return false
        return true

    return all(check(part) for part in sequence.strip().split(' '))

def parse_scramble(scramble):
    """Parses the given algorithm."""
    moves = []

    for move in scramble.strip().split(' '):
        if len(move.strip()) > 0:
            moveNum = 'FRUBLD'.index(move[0])
            power = 0

            if len(move) == 2:
                if move[1] == '2':
                    power = 1
                elif move[1] == '\'':
                    power = 2

            moves.append(moveNum * 3 + power)

    return moves

def format_move_sequence(moves):
    """Takes a sequence of moves as stored internally and returns a
    properly formatted sequence of moves.
    """
    sequence = ''

    first = True

    for move in moves:
        if first:
            first = False
        else:
            sequence += ' '

        sequence += 'FRUBLD'[move // 3]

        if move % 3 == 1:
            sequence += '2'
        elif move % 3 == 2:
            sequence += '\''

    return sequence
