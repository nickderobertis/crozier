

import typing

from .cat import Cat
from .dog import Dog

Pet = typing.Union[Cat, Dog]
