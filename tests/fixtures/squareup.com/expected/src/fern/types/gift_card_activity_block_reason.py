

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GiftCardActivityBlockReason(str, enum.Enum):
    """ """

    CHARGEBACK_BLOCK = "CHARGEBACK_BLOCK"

    def visit(self, chargeback_block: typing.Callable[[], T_Result]) -> T_Result:
        if self is GiftCardActivityBlockReason.CHARGEBACK_BLOCK:
            return chargeback_block()
