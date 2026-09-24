

import typing

from .v1project_cost_amount import V1ProjectCostAmount
from .v1project_cost_one import V1ProjectCostOne

V1ProjectCost = typing.Union[V1ProjectCostAmount, V1ProjectCostOne]
