from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    """
    Util class for using PriorityQueue.

    Attributes:
        priority (int): the priority.
        item (Any): the data of the item, with a non compare field.
    """
    priority: int
    item: Any=field(compare=False)