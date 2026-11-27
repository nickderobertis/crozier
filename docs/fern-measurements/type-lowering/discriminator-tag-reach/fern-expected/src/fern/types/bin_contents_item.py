

import typing

from .bolt_part import BoltPart
from .nut_part import NutPart

BinContentsItem = typing.Union[BoltPart, NutPart]
