

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ThreadStreamEventEvent(enum.StrEnum):
    THREAD_CREATED = "thread.created"

    def visit(self, thread_created: typing.Callable[[], T_Result]) -> T_Result:
        if self is ThreadStreamEventEvent.THREAD_CREATED:
            return thread_created()
