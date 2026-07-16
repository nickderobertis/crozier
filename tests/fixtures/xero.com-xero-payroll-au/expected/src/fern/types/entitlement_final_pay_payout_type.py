

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EntitlementFinalPayPayoutType(str, enum.Enum):
    NOTPAIDOUT = "NOTPAIDOUT"
    PAIDOUT = "PAIDOUT"

    def visit(self, notpaidout: typing.Callable[[], T_Result], paidout: typing.Callable[[], T_Result]) -> T_Result:
        if self is EntitlementFinalPayPayoutType.NOTPAIDOUT:
            return notpaidout()
        if self is EntitlementFinalPayPayoutType.PAIDOUT:
            return paidout()
