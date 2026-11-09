

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RunObjectObject(enum.StrEnum):
    """
    The object type, which is always `thread.run`.
    """

    THREAD_RUN = "thread.run"

    def visit(self, thread_run: typing.Callable[[], T_Result]) -> T_Result:
        if self is RunObjectObject.THREAD_RUN:
            return thread_run()
