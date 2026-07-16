

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostGetStackPolicyRequestAction(enum.StrEnum):
    GET_STACK_POLICY = "GetStackPolicy"

    def visit(self, get_stack_policy: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostGetStackPolicyRequestAction.GET_STACK_POLICY:
            return get_stack_policy()
