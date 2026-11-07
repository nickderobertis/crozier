

import typing

from .search_mode_hybrid import SearchModeHybrid
from .search_mode_vector import SearchModeVector
from .search_mode_zero import SearchModeZero

SearchMode = typing.Union[SearchModeZero, SearchModeVector, SearchModeHybrid]
