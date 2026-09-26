

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EventFileWatcherUpdatedPropertiesEventOne(enum.StrEnum):
    CHANGE = "change"

    def visit(self, change: typing.Callable[[], T_Result]) -> T_Result:
        if self is EventFileWatcherUpdatedPropertiesEventOne.CHANGE:
            return change()
