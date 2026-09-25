

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateMessageFlagsForNarrowRequestOp(enum.StrEnum):
    """
    Whether to `add` the flag or `remove` it.
    """

    ADD = "add"
    REMOVE = "remove"

    def visit(self, add: typing.Callable[[], T_Result], remove: typing.Callable[[], T_Result]) -> T_Result:
        if self is UpdateMessageFlagsForNarrowRequestOp.ADD:
            return add()
        if self is UpdateMessageFlagsForNarrowRequestOp.REMOVE:
            return remove()
