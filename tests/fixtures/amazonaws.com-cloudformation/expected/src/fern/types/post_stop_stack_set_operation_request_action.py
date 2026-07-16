

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostStopStackSetOperationRequestAction(str, enum.Enum):
    STOP_STACK_SET_OPERATION = "StopStackSetOperation"

    def visit(self, stop_stack_set_operation: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostStopStackSetOperationRequestAction.STOP_STACK_SET_OPERATION:
            return stop_stack_set_operation()
