

import typing

from .mordant import Mordant
from .shade_one import ShadeOne

Shade = typing.Union[Mordant, ShadeOne, str]
