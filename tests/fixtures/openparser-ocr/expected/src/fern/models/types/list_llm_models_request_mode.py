

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListLlmModelsRequestMode(enum.StrEnum):
    SUGGESTED = "suggested"
    SEARCH = "search"

    def visit(self, suggested: typing.Callable[[], T_Result], search: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListLlmModelsRequestMode.SUGGESTED:
            return suggested()
        if self is ListLlmModelsRequestMode.SEARCH:
            return search()
