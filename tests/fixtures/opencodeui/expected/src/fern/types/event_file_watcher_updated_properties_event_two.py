

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EventFileWatcherUpdatedPropertiesEventTwo(enum.StrEnum):
    UNLINK = "unlink"

    def visit(self, unlink: typing.Callable[[], T_Result]) -> T_Result:
        if self is EventFileWatcherUpdatedPropertiesEventTwo.UNLINK:
            return unlink()
