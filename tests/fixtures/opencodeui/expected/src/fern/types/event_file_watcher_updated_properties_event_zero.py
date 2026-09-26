

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EventFileWatcherUpdatedPropertiesEventZero(enum.StrEnum):
    ADD = "add"

    def visit(self, add: typing.Callable[[], T_Result]) -> T_Result:
        if self is EventFileWatcherUpdatedPropertiesEventZero.ADD:
            return add()
