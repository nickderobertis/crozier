

import typing

from .v1project_profit_amount import V1ProjectProfitAmount
from .v1project_profit_one import V1ProjectProfitOne

V1ProjectProfit = typing.Union[V1ProjectProfitAmount, V1ProjectProfitOne]
