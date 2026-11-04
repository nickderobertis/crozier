

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EventType(enum.StrEnum):
    """
    Event types.
    """

    TEST = "test"

    def visit(self, test: typing.Callable[[], T_Result]) -> T_Result:
        if self is EventType.TEST:
            return test()
