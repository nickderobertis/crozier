

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EnrichTransactionDirection(enum.StrEnum):
    """
    The direction of the transaction from the perspective of the account holder:

    `OUTFLOW` - Includes outgoing transfers, purchases, and fees. (Typically represented as a negative value on checking accounts and debit cards and a positive value on credit cards.)

    `INFLOW` - Includes incoming transfers, refunds, and income. (Typically represented as a positive value on checking accounts and debit cards and a negative value on credit cards.)
    """

    INFLOW = "INFLOW"
    OUTFLOW = "OUTFLOW"

    def visit(self, inflow: typing.Callable[[], T_Result], outflow: typing.Callable[[], T_Result]) -> T_Result:
        if self is EnrichTransactionDirection.INFLOW:
            return inflow()
        if self is EnrichTransactionDirection.OUTFLOW:
            return outflow()
