from typing import List, Optional

class Node:
    """
    A point in time on the board.
    """
    def __init__(self, state: List[int], parent: Optional['Node'], depth: int):
        """
        Args:
            state (List[int]): the state of the board in the given time, will be used for history.
            parent (Optional[Node]): previous node.
            depth (int): how many moves were executed before this node.
        """
        self.state = state
        self.parent = parent
        self.depth = depth
    
    def trace_path(self) -> List[int]:
        """
        Traces the path from the current node to the start.

        Returns:
            List[int]: the solution to the board (history of the nodes reversed).
        """
        path = []
        current = self

        while current.parent is not None:
            path.append(current.parent.state[current.state.index(0)])
            current = current.parent

        return path[::-1]
    