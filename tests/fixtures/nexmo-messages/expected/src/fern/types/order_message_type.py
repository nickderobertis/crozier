

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OrderMessageType(enum.StrEnum):
    """
    The type of message to send.
    """

    ORDER = "order"

    def visit(self, order: typing.Callable[[], T_Result]) -> T_Result:
        if self is OrderMessageType.ORDER:
            return order()
