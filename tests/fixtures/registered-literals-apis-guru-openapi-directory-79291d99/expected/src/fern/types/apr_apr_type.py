

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AprAprType(enum.StrEnum):
    """
    The type of balance to which the APR applies.
    """

    BALANCE_TRANSFER_APR = "balance_transfer_apr"
    CASH_APR = "cash_apr"
    PURCHASE_APR = "purchase_apr"
    SPECIAL = "special"

    def visit(
        self,
        balance_transfer_apr: typing.Callable[[], T_Result],
        cash_apr: typing.Callable[[], T_Result],
        purchase_apr: typing.Callable[[], T_Result],
        special: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AprAprType.BALANCE_TRANSFER_APR:
            return balance_transfer_apr()
        if self is AprAprType.CASH_APR:
            return cash_apr()
        if self is AprAprType.PURCHASE_APR:
            return purchase_apr()
        if self is AprAprType.SPECIAL:
            return special()
