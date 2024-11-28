from typing import List, Generator
from .node import Node
from .action import Action
from .algorithm import Algorithm

# Constants
BOARD_GOAL = list(range(0, 9)) # Desired Board State
ROW_LENGTH = 3
COLUMN_LENGTH = 3

class Board:
    """
    the "Main" entity of the program, holds the state of the board and solves it in various ways.
    """
    def __init__(self, initial_state: List[int]):
        """
        Args:
            initial_state (List[int]): the user provided board state.
        """
        self.initial_state = initial_state

    def solve(self) -> None:
        """
        Runs through the program algorithms and solves the board in each way.
        """
        for alg in Algorithm:
            name = alg.name if alg.name != 'A' else 'A*'
            target_node, iterations, found_path = alg.value(self)
            print(f'{name:8} {iterations:8}', end='  ')

            if found_path:
                print(target_node.trace_path())
            else:
                print("path wan't found")


    @staticmethod
    def goal_reached(state: List[int]) -> bool:
        """
        Checks whether or not a given state is a completed state.

        Args:
            state (List[int]): the state to check.

        Returns:
            bool: True if the board is solved.
        """
        return state == BOARD_GOAL
    
    def generate_children(self, node: Node) -> Generator[Node, None, None]:
        """
        Generates the possible move on the board on a given node and yields it;

        Args:
            node (Node): the node to check for.

        Returns:
            Generator[Node, None, None]: a yielded node of the next possible move.
        """
        actionService = Action(node)

        for action in [
            actionService.up, 
            actionService.down, 
            actionService.left, 
            actionService.right
            ]:

            next_state = action()
            if next_state:
                yield Node(
                    state=next_state,
                    parent=node,
                    depth=node.depth + 1,
                )