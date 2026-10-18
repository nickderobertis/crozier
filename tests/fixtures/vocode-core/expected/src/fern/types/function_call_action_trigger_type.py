

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FunctionCallActionTriggerType(enum.StrEnum):
    ACTION_TRIGGER_FUNCTION_CALL = "action_trigger_function_call"

    def visit(self, action_trigger_function_call: typing.Callable[[], T_Result]) -> T_Result:
        if self is FunctionCallActionTriggerType.ACTION_TRIGGER_FUNCTION_CALL:
            return action_trigger_function_call()
