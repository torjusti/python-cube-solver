import re

def validate_sequence(sequence):
  if len(sequence.trim()) == 0: return false

  def check(part):
    if len(part.trim()) == 0: return true
    if !re.match("^[FRUBLD]{1}[2']?", part): return false
    return true

  return all(check(part) for part in sequence.trim().split(' '))

def parse_scramble():
    moves = []

    for move in scramble.trim().split(' '):
        if len(move.trim()) > 0:
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
