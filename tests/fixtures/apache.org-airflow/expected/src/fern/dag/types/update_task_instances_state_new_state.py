

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateTaskInstancesStateNewState(enum.StrEnum):
    """
    Expected new state.
    """

    SUCCESS = "success"
    FAILED = "failed"

    def visit(self, success: typing.Callable[[], T_Result], failed: typing.Callable[[], T_Result]) -> T_Result:
        if self is UpdateTaskInstancesStateNewState.SUCCESS:
            return success()
        if self is UpdateTaskInstancesStateNewState.FAILED:
            return failed()
