

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RunObjectRequiredActionType(enum.StrEnum):
    """
    For now, this is always `submit_tool_outputs`.
    """

    SUBMIT_TOOL_OUTPUTS = "submit_tool_outputs"

    def visit(self, submit_tool_outputs: typing.Callable[[], T_Result]) -> T_Result:
        if self is RunObjectRequiredActionType.SUBMIT_TOOL_OUTPUTS:
            return submit_tool_outputs()
