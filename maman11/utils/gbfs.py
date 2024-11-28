import classes.board as board
from typing import Tuple, Optional
from classes.node import Node
from .best_first_search import linear_conflicts, best_first_search

def gbfs_search(board: 'board.board') -> Tuple[Optional[Node], int, bool]:
    """
    solving the board using GBFS algorithm via section 3.5.1.

    Args:
        board (Board): the starting board.
    
    Returns:
        Tuple[Optional[Node], int, bool]: (
            - the final node in case we solved it.
            - number of iterations.
            - an indication whether or not we solved the board.
        )
    """
    return best_first_search(board, linear_conflicts)
