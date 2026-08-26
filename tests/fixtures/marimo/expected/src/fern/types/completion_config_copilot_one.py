

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CompletionConfigCopilotOne(enum.StrEnum):
    CODEIUM = "codeium"
    CUSTOM = "custom"
    GITHUB = "github"

    def visit(
        self,
        codeium: typing.Callable[[], T_Result],
        custom: typing.Callable[[], T_Result],
        github: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CompletionConfigCopilotOne.CODEIUM:
            return codeium()
        if self is CompletionConfigCopilotOne.CUSTOM:
            return custom()
        if self is CompletionConfigCopilotOne.GITHUB:
            return github()
