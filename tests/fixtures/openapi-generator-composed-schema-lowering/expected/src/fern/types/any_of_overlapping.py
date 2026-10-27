

import typing

from .overlapping_object_a import OverlappingObjectA
from .overlapping_object_b import OverlappingObjectB

AnyOfOverlapping = typing.Union[OverlappingObjectA, OverlappingObjectB]
