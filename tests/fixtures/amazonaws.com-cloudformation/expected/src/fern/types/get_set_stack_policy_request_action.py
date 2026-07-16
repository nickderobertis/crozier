

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetSetStackPolicyRequestAction(enum.StrEnum):
    SET_STACK_POLICY = "SetStackPolicy"

    def visit(self, set_stack_policy: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetSetStackPolicyRequestAction.SET_STACK_POLICY:
            return set_stack_policy()
