

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetUpdateStackSetRequestAction(str, enum.Enum):
    UPDATE_STACK_SET = "UpdateStackSet"

    def visit(self, update_stack_set: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetUpdateStackSetRequestAction.UPDATE_STACK_SET:
            return update_stack_set()
