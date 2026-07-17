

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OrderFulfillmentState(enum.StrEnum):
    """
    The current state of this fulfillment.
    """

    PROPOSED = "PROPOSED"
    RESERVED = "RESERVED"
    PREPARED = "PREPARED"
    COMPLETED = "COMPLETED"
    CANCELED = "CANCELED"
    FAILED = "FAILED"

    def visit(
        self,
        proposed: typing.Callable[[], T_Result],
        reserved: typing.Callable[[], T_Result],
        prepared: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        canceled: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OrderFulfillmentState.PROPOSED:
            return proposed()
        if self is OrderFulfillmentState.RESERVED:
            return reserved()
        if self is OrderFulfillmentState.PREPARED:
            return prepared()
        if self is OrderFulfillmentState.COMPLETED:
            return completed()
        if self is OrderFulfillmentState.CANCELED:
            return canceled()
        if self is OrderFulfillmentState.FAILED:
            return failed()
