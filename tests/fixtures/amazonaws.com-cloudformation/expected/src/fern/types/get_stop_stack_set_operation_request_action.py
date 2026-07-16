

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetStopStackSetOperationRequestAction(enum.StrEnum):
    STOP_STACK_SET_OPERATION = "StopStackSetOperation"

    def visit(self, stop_stack_set_operation: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetStopStackSetOperationRequestAction.STOP_STACK_SET_OPERATION:
            return stop_stack_set_operation()
