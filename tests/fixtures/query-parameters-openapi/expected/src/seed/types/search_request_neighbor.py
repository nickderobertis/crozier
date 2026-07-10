

import typing

from .nested_user import NestedUser
from .user import User

SearchRequestNeighbor = typing.Union[User, NestedUser, str, int]
