

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetFamilyBalancesV3RequestView(enum.StrEnum):
    TRANSACTIONS = "transactions"

    def visit(self, transactions: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetFamilyBalancesV3RequestView.TRANSACTIONS:
            return transactions()
