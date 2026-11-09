

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WarningWarningCode(enum.StrEnum):
    """
    The warning code identifies a specific kind of warning. `OWNERS_UNAVAILABLE` indicates that account-owner information is not available.`INVESTMENTS_UNAVAILABLE` indicates that Investments specific information is not available. `TRANSACTIONS_UNAVAILABLE` indicates that transactions information associated with Credit and Depository accounts are unavailable.
    """

    OWNERS_UNAVAILABLE = "OWNERS_UNAVAILABLE"
    INVESTMENTS_UNAVAILABLE = "INVESTMENTS_UNAVAILABLE"
    TRANSACTIONS_UNAVAILABLE = "TRANSACTIONS_UNAVAILABLE"

    def visit(
        self,
        owners_unavailable: typing.Callable[[], T_Result],
        investments_unavailable: typing.Callable[[], T_Result],
        transactions_unavailable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WarningWarningCode.OWNERS_UNAVAILABLE:
            return owners_unavailable()
        if self is WarningWarningCode.INVESTMENTS_UNAVAILABLE:
            return investments_unavailable()
        if self is WarningWarningCode.TRANSACTIONS_UNAVAILABLE:
            return transactions_unavailable()
