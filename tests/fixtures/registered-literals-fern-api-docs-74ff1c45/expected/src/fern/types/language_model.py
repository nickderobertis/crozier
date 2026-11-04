

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LanguageModel(enum.StrEnum):
    CLAUDE4SONNET = "claude-4-sonnet"
    CLAUDE45HAIKU = "claude-4.5-haiku"
    CLAUDE45SONNET = "claude-4.5-sonnet"
    CLAUDE46SONNET = "claude-4.6-sonnet"

    def visit(
        self,
        claude4sonnet: typing.Callable[[], T_Result],
        claude45haiku: typing.Callable[[], T_Result],
        claude45sonnet: typing.Callable[[], T_Result],
        claude46sonnet: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LanguageModel.CLAUDE4SONNET:
            return claude4sonnet()
        if self is LanguageModel.CLAUDE45HAIKU:
            return claude45haiku()
        if self is LanguageModel.CLAUDE45SONNET:
            return claude45sonnet()
        if self is LanguageModel.CLAUDE46SONNET:
            return claude46sonnet()
