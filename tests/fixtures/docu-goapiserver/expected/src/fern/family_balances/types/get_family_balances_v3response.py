

import typing

from ...types.family_balance import FamilyBalance
from ...types.family_balance_aggregate import FamilyBalanceAggregate
from ...types.family_ledger import FamilyLedger

GetFamilyBalancesV3Response = typing.Union[
    typing.List[FamilyBalance], typing.List[FamilyBalanceAggregate], typing.List[FamilyLedger]
]
