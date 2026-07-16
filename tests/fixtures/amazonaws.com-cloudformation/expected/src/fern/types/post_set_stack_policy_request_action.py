

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostSetStackPolicyRequestAction(str, enum.Enum):
    SET_STACK_POLICY = "SetStackPolicy"

    def visit(self, set_stack_policy: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostSetStackPolicyRequestAction.SET_STACK_POLICY:
            return set_stack_policy()
