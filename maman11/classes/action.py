from typing import List, Optional
from .node import Node

class Action:
    """
    A class responsible for moving tiles around the board.
    """
    def __init__(self, node: Node):
        """
        Args:
            node (Node): the wanted node to move
        """
        self.node_state = node.state
        self.empty_idx = node.state.index(0)

    def __swap_positions(self, index1: int, index2: int) -> Optional[List[int]]:
        """
        private function responsible for moving empty tile;

        Args:
            index1 (int): empty tile index,
            index2 (int): wanted tile to move.

        Returns:
            Optional[List[int]]: the new state of the board;
        """
        if 0 <= index1 < len(self.node_state) and 0 <= index2 < len(self.node_state):
            new_state = self.node_state.copy()
            new_state[index1], new_state[index2] = new_state[index2], new_state[index1]
            return new_state
        
        return None

    def up(self) -> Optional[List[int]]:
        """
        Moves the blank tile up if possible.

        Returns:
            Optional[List[int]]: the new state of the board;
        """
        if self.empty_idx < 3:
            return None
        
        return self.__swap_positions(self.empty_idx, self.empty_idx - 3)
    
    def down(self) -> Optional[List[int]]:
        """
        Moves the blank tile down if possible.

        Returns:
            Optional[List[int]]: the new state of the board;
        """
        if self.empty_idx > 5:
            return None
        
        return self.__swap_positions(self.empty_idx, self.empty_idx + 3)
    
    def left(self) -> Optional[List[int]]:
        """
        Moves the blank tile left if possible.

        Returns:
            Optional[List[int]]: the new state of the board;
        """
        if self.empty_idx % 3 == 0:
            return None
        
        return self.__swap_positions(self.empty_idx, self.empty_idx - 1)
    
    def right(self) -> Optional[List[int]]:
        """
        Moves the blank tile right if possible.

        Returns:
            Optional[List[int]]: the new state of the board;
        """
        if self.empty_idx % 3 == 2:
            return None
        
        return self.__swap_positions(self.empty_idx, self.empty_idx + 1)