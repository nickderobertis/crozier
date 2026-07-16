

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostGetStackPolicyRequestAction(str, enum.Enum):
    GET_STACK_POLICY = "GetStackPolicy"

    def visit(self, get_stack_policy: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostGetStackPolicyRequestAction.GET_STACK_POLICY:
            return get_stack_policy()
