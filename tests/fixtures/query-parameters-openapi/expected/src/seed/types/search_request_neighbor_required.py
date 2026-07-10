

import typing

from .nested_user import NestedUser
from .user import User

SearchRequestNeighborRequired = typing.Union[User, NestedUser, str, int]
