

import typing

from .barge import Barge
from .sailboat import Sailboat

Vessel = typing.Union[Sailboat, Barge]
