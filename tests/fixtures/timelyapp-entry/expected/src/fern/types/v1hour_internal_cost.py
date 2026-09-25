

import typing

from .v1hour_internal_cost_amount import V1HourInternalCostAmount
from .v1hour_internal_cost_one import V1HourInternalCostOne

V1HourInternalCost = typing.Union[V1HourInternalCostAmount, V1HourInternalCostOne]
