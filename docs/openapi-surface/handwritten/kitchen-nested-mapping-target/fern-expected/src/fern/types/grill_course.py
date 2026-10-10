

import typing

from .skewer_order import SkewerOrder
from .steak_order import SteakOrder

GrillCourse = typing.Union[SteakOrder, SkewerOrder]
