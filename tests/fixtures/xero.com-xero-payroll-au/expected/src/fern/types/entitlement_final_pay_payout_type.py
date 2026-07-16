

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EntitlementFinalPayPayoutType(enum.StrEnum):
    NOTPAIDOUT = "NOTPAIDOUT"
    PAIDOUT = "PAIDOUT"

    def visit(self, notpaidout: typing.Callable[[], T_Result], paidout: typing.Callable[[], T_Result]) -> T_Result:
        if self is EntitlementFinalPayPayoutType.NOTPAIDOUT:
            return notpaidout()
        if self is EntitlementFinalPayPayoutType.PAIDOUT:
            return paidout()
