

import typing

from .v1project_internal_cost_amount import V1ProjectInternalCostAmount
from .v1project_internal_cost_one import V1ProjectInternalCostOne

V1ProjectInternalCost = typing.Union[V1ProjectInternalCostAmount, V1ProjectInternalCostOne]
