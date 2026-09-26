

import typing

from .v1project_unbilled_cost_amount import V1ProjectUnbilledCostAmount
from .v1project_unbilled_cost_one import V1ProjectUnbilledCostOne

V1ProjectUnbilledCost = typing.Union[V1ProjectUnbilledCostAmount, V1ProjectUnbilledCostOne]
