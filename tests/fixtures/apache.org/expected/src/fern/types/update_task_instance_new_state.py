

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class UpdateTaskInstanceNewState(str, enum.Enum):
    """
    Expected new state.
    """

    SUCCESS = "success"
    FAILED = "failed"

    def visit(self, success: typing.Callable[[], T_Result], failed: typing.Callable[[], T_Result]) -> T_Result:
        if self is UpdateTaskInstanceNewState.SUCCESS:
            return success()
        if self is UpdateTaskInstanceNewState.FAILED:
            return failed()
