

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class OrderState(str, enum.Enum):
    """
    The state of the order.
    """

    OPEN = "OPEN"
    COMPLETED = "COMPLETED"
    CANCELED = "CANCELED"

    def visit(
        self,
        open: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        canceled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OrderState.OPEN:
            return open()
        if self is OrderState.COMPLETED:
            return completed()
        if self is OrderState.CANCELED:
            return canceled()
