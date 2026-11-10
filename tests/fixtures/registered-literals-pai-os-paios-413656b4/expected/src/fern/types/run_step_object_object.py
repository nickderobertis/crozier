

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RunStepObjectObject(enum.StrEnum):
    """
    The object type, which is always `thread.run.step`.
    """

    THREAD_RUN_STEP = "thread.run.step"

    def visit(self, thread_run_step: typing.Callable[[], T_Result]) -> T_Result:
        if self is RunStepObjectObject.THREAD_RUN_STEP:
            return thread_run_step()
