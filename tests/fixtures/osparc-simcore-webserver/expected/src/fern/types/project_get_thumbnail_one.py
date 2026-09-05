

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProjectGetThumbnailOne(enum.StrEnum):
    EMPTY = ""

    def visit(self, empty: typing.Callable[[], T_Result]) -> T_Result:
        if self is ProjectGetThumbnailOne.EMPTY:
            return empty()
