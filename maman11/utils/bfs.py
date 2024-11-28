import classes.board as board
from typing import Tuple, Optional
from collections import deque 
from classes.node import Node

def bfs_search(board: 'board.Board') -> Tuple[Optional[Node], int, bool]:
    """
    solving the board using BFS algorithm via figure 3.9.

    Args:
        board (Board): the starting board.
    
    Returns:
        Tuple[Optional[Node], int, bool]: (
            - the final node in case we solved it.
            - number of iterations.
            - an indication whether or not we solved the board.
        )
    """
    start_node = Node(board.initial_state, None, 0)

    if board.goal_reached(start_node.state):
        return start_node, 0, True

    queue = deque([start_node])
    seen_states = {tuple(board.initial_state)}
    iterations = 0

    while queue:
        current_node = queue.pop()
        iterations += 1

        for child_node in board.generate_children(current_node):
            if board.goal_reached(child_node.state):
                return child_node, iterations, True
            
            if tuple(child_node.state) not in seen_states:
                seen_states.add(tuple(child_node.state))
                queue.appendleft(child_node)

    return None, iterations, False