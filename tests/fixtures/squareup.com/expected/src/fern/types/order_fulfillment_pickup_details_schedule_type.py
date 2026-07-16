

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class OrderFulfillmentPickupDetailsScheduleType(str, enum.Enum):
    """
    The schedule type of the pickup fulfillment.
    """

    SCHEDULED = "SCHEDULED"
    ASAP = "ASAP"

    def visit(self, scheduled: typing.Callable[[], T_Result], asap: typing.Callable[[], T_Result]) -> T_Result:
        if self is OrderFulfillmentPickupDetailsScheduleType.SCHEDULED:
            return scheduled()
        if self is OrderFulfillmentPickupDetailsScheduleType.ASAP:
            return asap()
