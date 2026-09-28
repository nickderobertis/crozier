

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PromptsPromptNamePostError400ErrorCode(enum.StrEnum):
    VALIDATION_ERROR = "VALIDATION_ERROR"

    def visit(self, validation_error: typing.Callable[[], T_Result]) -> T_Result:
        if self is PromptsPromptNamePostError400ErrorCode.VALIDATION_ERROR:
            return validation_error()
