

import typing

from .harvest_board_harvests import HarvestBoardHarvests
from .harvest_board_zero import HarvestBoardZero

HarvestBoard = typing.Union[HarvestBoardZero, HarvestBoardHarvests]
