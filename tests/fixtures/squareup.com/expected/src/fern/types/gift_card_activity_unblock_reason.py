

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GiftCardActivityUnblockReason(enum.StrEnum):
    """ """

    CHARGEBACK_UNBLOCK = "CHARGEBACK_UNBLOCK"

    def visit(self, chargeback_unblock: typing.Callable[[], T_Result]) -> T_Result:
        if self is GiftCardActivityUnblockReason.CHARGEBACK_UNBLOCK:
            return chargeback_unblock()
