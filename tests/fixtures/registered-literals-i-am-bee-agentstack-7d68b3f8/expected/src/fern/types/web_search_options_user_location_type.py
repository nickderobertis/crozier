

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WebSearchOptionsUserLocationType(enum.StrEnum):
    APPROXIMATE = "approximate"

    def visit(self, approximate: typing.Callable[[], T_Result]) -> T_Result:
        if self is WebSearchOptionsUserLocationType.APPROXIMATE:
            return approximate()
