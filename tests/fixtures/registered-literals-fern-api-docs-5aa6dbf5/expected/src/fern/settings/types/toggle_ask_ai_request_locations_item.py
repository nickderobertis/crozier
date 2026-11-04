

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ToggleAskAiRequestLocationsItem(enum.StrEnum):
    DOCS = "docs"
    SLACK = "slack"

    def visit(self, docs: typing.Callable[[], T_Result], slack: typing.Callable[[], T_Result]) -> T_Result:
        if self is ToggleAskAiRequestLocationsItem.DOCS:
            return docs()
        if self is ToggleAskAiRequestLocationsItem.SLACK:
            return slack()
