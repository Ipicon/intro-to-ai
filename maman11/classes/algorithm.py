from enum import Enum
from functools import partial
from utils.bfs import bfs_search
from utils.iddfs import iddfs_search
from utils.gbfs import gbfs_search
from utils.a_star import a_star_search

class Algorithm(Enum):
    """
    an enum class responsible for holding all algorithms we want to run on our board to solve it.
    """
    BFS = partial(bfs_search) # using partials so python considers them as attributes and not functions
    IDDFS = partial(iddfs_search)
    GBFS = partial(gbfs_search)
    A = partial(a_star_search)