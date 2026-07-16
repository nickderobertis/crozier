

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GiftCardActivityUnblockReason(str, enum.Enum):
    """ """

    CHARGEBACK_UNBLOCK = "CHARGEBACK_UNBLOCK"

    def visit(self, chargeback_unblock: typing.Callable[[], T_Result]) -> T_Result:
        if self is GiftCardActivityUnblockReason.CHARGEBACK_UNBLOCK:
            return chargeback_unblock()
