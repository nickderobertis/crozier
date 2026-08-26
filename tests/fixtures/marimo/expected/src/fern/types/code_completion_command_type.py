

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CodeCompletionCommandType(enum.StrEnum):
    CODE_COMPLETION = "code-completion"

    def visit(self, code_completion: typing.Callable[[], T_Result]) -> T_Result:
        if self is CodeCompletionCommandType.CODE_COMPLETION:
            return code_completion()
