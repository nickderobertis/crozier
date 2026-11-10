

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BankTransferDirection(enum.StrEnum):
    """
    Indicates the direction of the transfer: `outbound` for API-initiated transfers, or `inbound` for payments received by the FBO account.
    """

    OUTBOUND = "outbound"
    INBOUND = "inbound"

    def visit(self, outbound: typing.Callable[[], T_Result], inbound: typing.Callable[[], T_Result]) -> T_Result:
        if self is BankTransferDirection.OUTBOUND:
            return outbound()
        if self is BankTransferDirection.INBOUND:
            return inbound()
