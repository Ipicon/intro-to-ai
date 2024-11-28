import classes.board as board
from classes.node import Node
from typing import Tuple, Optional, Set, List

def _dls(board: 'board.Board', node: Node, depth: int, visited: Set[Tuple]) -> Tuple[Optional[Node], int, bool, bool]:
    """
    A depth limited search.

    Args:
        board (Board): the starting board.
        node (Node): current node in time.
        depth (int): the depth of the dls algorithm.
        visited (Set[Tuple]): which states were visited in the current depth iteration.
    
    Returns:
        Tuple[Optional[Node], int, bool, bool]: (
            - the final node in case we solved it.
            - number of iterations.
            - an indication whether or not we solved the board.
        )
    """
    if board.goal_reached(node.state):
        return node, 1, True
    
    if depth == 0:
        return None, 0, False
    
    visited.add(tuple(node.state))
    iterations = 0
    
    for child_node in board.generate_children(node):
        if tuple(child_node.state) not in visited:
            result, expanded, isFound = _dls(board, child_node, depth - 1, visited)
            iterations += expanded

            if isFound:
                return result, iterations, True

    visited.remove(tuple(node.state))
    return None, iterations + 1, False

def iddfs_search(board: 'board.Board') -> Tuple[Optional[Node], int, bool]:
    """
    solving the board using IDDFS algorithm via figure 3.12.

    Args:
        board (Board): the starting board.
    
    Returns:
        Tuple[Optional[Node], int, bool]: (
            - the final node in case we solved it.
            - number of iterations.
            - an indication whether or not we solved the board.
        )
    """
    depth = 0
    iterations = 0 

    while True:
        visited = set()

        result, expanded, isFound = _dls(board, Node(
             state=board.initial_state,
             parent=None,
             depth=0
        ), depth, visited)

        iterations += expanded

        if isFound:
             return result, iterations, True
        
        depth += 1