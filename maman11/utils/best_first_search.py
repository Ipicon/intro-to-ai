import classes.board as board
from typing import Tuple, Optional, List, Literal, Callable
from queue import PriorityQueue
from classes.node import Node
from classes.prioritized_item import PrioritizedItem

def _manhattan_distance(state: List[int]) -> int:
        """
        calculates the manhattan distance.

        Args:
            state (List[int]): state of the board in a given node.

        Args:
            int: so called distance.
        """
        distance = 0

        for idx, tile in enumerate(state):
            goal_row, goal_col = divmod(tile, 3)
            current_row, current_col = divmod(idx, 3)
            distance += abs(goal_row - current_row) + abs(goal_col - current_col)

        return distance

def _search_conflicts(state: List[int], mode = Literal['col', 'row']) -> int:
        """
        searches for collisions after calculating the manhattan distance.

        Args:
            state (List[int]): state of the board in a given node.
            mode (Literal['col', 'row]): the way we should calculate the current collisions.

        Returns:
            int: num of collisions.
        """
        sum = 0
        
        for line in range(board.ROW_LENGTH):
            if mode == 'row':
                curr_line = state[line * board.ROW_LENGTH:(line +1) * board.ROW_LENGTH]
            else:
                 curr_line = state[line::board.COLUMN_LENGTH]

            for opposite_line, tile1 in enumerate(curr_line):
                for tile2 in curr_line[opposite_line:]:
                    if (tile1 != 0 and 
                        tile2 != 0):
                        if ((mode == 'row' and
                            line == (tile1 // 3) and
                            line == (tile2 // 3) and
                            (tile1 % 3) > (tile2 % 3)) or 
                            (mode == 'col' and
                            line == (tile1 % 3) and
                            line == (tile2 % 3) and
                            (tile1 // 3) > (tile2 // 3))):
                            sum += 2
        return sum

def linear_conflicts(node: Node) -> int:
    """
    Calculates the linear conflicts distance on a board.

    Args:
        node (Node): the node to calculate against.
    
    Returns:
        int: the number of conflicts.
    """
    return _manhattan_distance(node.state) + _search_conflicts(node.state, 'row') + _search_conflicts(node.state, 'col')

def best_first_search(board: 'board.Board', priority_func:  Callable[[Node], int]) -> Tuple[Optional[Node], int, bool]:
    """
    A class of search algorithms which explores a graph by expanding the most promising node chosen according to a specified rule.

    Args:
        board (Board): the starting board.
        priority_func (Callable[[Node], int]): a function to decided the priority of a node.

    Returns:
        Tuple[Optional[Node], int, bool]: (
            - the final node in case we solved it.
            - number of iterations.
            - an indication whether or not we solved the board.
        )
    """
    start_node = Node(board.initial_state, None, 0)

    queue = PriorityQueue()
    queue.put(PrioritizedItem(priority_func(start_node), start_node))

    seen_states = {tuple(board.initial_state): start_node}
    iterations = 0

    while queue:
        iterations += 1
        node = queue.get().item

        if board.goal_reached(node.state):
              return node, iterations, True
        for child_node in board.generate_children(node):
            current_state = tuple(child_node.state)

            if (tuple(current_state) not in seen_states or
                seen_states[current_state].depth > child_node.depth):
                    seen_states[current_state] = child_node
                    queue.put(PrioritizedItem(priority_func(child_node), child_node))


            
    return None, iterations, False
