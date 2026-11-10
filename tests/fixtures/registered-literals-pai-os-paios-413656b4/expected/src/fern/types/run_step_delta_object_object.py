

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RunStepDeltaObjectObject(enum.StrEnum):
    """
    The object type, which is always `thread.run.step.delta`.
    """

    THREAD_RUN_STEP_DELTA = "thread.run.step.delta"

    def visit(self, thread_run_step_delta: typing.Callable[[], T_Result]) -> T_Result:
        if self is RunStepDeltaObjectObject.THREAD_RUN_STEP_DELTA:
            return thread_run_step_delta()
