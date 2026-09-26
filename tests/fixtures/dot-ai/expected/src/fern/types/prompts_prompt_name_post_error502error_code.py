

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PromptsPromptNamePostError502ErrorCode(enum.StrEnum):
    PROMPTS_SOURCE_ERROR = "PROMPTS_SOURCE_ERROR"

    def visit(self, prompts_source_error: typing.Callable[[], T_Result]) -> T_Result:
        if self is PromptsPromptNamePostError502ErrorCode.PROMPTS_SOURCE_ERROR:
            return prompts_source_error()
