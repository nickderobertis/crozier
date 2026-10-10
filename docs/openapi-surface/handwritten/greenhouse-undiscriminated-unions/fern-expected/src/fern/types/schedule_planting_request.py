

import typing

from .cutting import Cutting
from .seedling import Seedling

SchedulePlantingRequest = typing.Union[Seedling, Cutting]
