

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PromptsGetError502ErrorCode(enum.StrEnum):
    PROMPTS_SOURCE_ERROR = "PROMPTS_SOURCE_ERROR"

    def visit(self, prompts_source_error: typing.Callable[[], T_Result]) -> T_Result:
        if self is PromptsGetError502ErrorCode.PROMPTS_SOURCE_ERROR:
            return prompts_source_error()
