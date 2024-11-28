import classes.board as board # imported like this to handle circular import dependencies
from typing import Tuple, Optional
from classes.node import Node
from .best_first_search import linear_conflicts, best_first_search

def a_star_search(board: 'board.board') -> Tuple[Optional[Node], int, bool]:
    """
    solving the board using A* algorithm via section 3.5.2.

    Args:
        board (Board): the starting board.
    
    Returns:
        Tuple[Optional[Node], int, bool]: (
            - the final node in case we solved it.
            - number of iterations.
            - an indication whether or not we solved the board.
        )
    """
    return best_first_search(board, lambda node: node.depth + linear_conflicts(node))
