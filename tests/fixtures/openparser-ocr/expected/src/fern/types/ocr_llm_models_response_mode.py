

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OcrLlmModelsResponseMode(enum.StrEnum):
    SUGGESTED = "suggested"
    SEARCH = "search"

    def visit(self, suggested: typing.Callable[[], T_Result], search: typing.Callable[[], T_Result]) -> T_Result:
        if self is OcrLlmModelsResponseMode.SUGGESTED:
            return suggested()
        if self is OcrLlmModelsResponseMode.SEARCH:
            return search()
