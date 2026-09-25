

import typing

from .v1project_billed_cost_amount import V1ProjectBilledCostAmount
from .v1project_billed_cost_one import V1ProjectBilledCostOne

V1ProjectBilledCost = typing.Union[V1ProjectBilledCostAmount, V1ProjectBilledCostOne]
