

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BankTransferEventListDirection(enum.StrEnum):
    """
    Indicates the direction of the transfer: `outbound`: for API-initiated transfers
    `inbound`: for payments received by the FBO account.
    """

    INBOUND = "inbound"
    OUTBOUND = "outbound"

    def visit(self, inbound: typing.Callable[[], T_Result], outbound: typing.Callable[[], T_Result]) -> T_Result:
        if self is BankTransferEventListDirection.INBOUND:
            return inbound()
        if self is BankTransferEventListDirection.OUTBOUND:
            return outbound()
