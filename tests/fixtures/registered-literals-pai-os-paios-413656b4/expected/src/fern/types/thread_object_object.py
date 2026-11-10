

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ThreadObjectObject(enum.StrEnum):
    """
    The object type, which is always `thread`.
    """

    THREAD = "thread"

    def visit(self, thread: typing.Callable[[], T_Result]) -> T_Result:
        if self is ThreadObjectObject.THREAD:
            return thread()
