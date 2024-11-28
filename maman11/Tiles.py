import sys
from classes.board import Board

if __name__ == '__main__':
    # we extract the user argument
    inputs = sys.argv[1:]
    bad_input = len(inputs) != 9
    
    for val in inputs:
        if not val.isnumeric():
            bad_input = True

    # in case we didn't get a correct input
    if bad_input:
        print('Bad user input.')
    else:
        board = Board([int(val) for val in inputs])
        board.solve()