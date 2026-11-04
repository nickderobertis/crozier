

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChatCompletionAllowedToolsParamMode(enum.StrEnum):
    AUTO = "auto"
    REQUIRED = "required"

    def visit(self, auto: typing.Callable[[], T_Result], required: typing.Callable[[], T_Result]) -> T_Result:
        if self is ChatCompletionAllowedToolsParamMode.AUTO:
            return auto()
        if self is ChatCompletionAllowedToolsParamMode.REQUIRED:
            return required()
