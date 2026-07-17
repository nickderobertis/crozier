

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GiftCardActivityBlockReason(enum.StrEnum):
    """ """

    CHARGEBACK_BLOCK = "CHARGEBACK_BLOCK"

    def visit(self, chargeback_block: typing.Callable[[], T_Result]) -> T_Result:
        if self is GiftCardActivityBlockReason.CHARGEBACK_BLOCK:
            return chargeback_block()
