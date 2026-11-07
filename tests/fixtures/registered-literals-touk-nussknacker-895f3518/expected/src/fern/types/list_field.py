

import typing

from .field import Field
from .nil import Nil

ListField = typing.Union[Nil, typing.List[Field]]
