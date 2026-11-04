

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WebSearchOptionsSearchContextSize(enum.StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

    def visit(
        self,
        low: typing.Callable[[], T_Result],
        medium: typing.Callable[[], T_Result],
        high: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WebSearchOptionsSearchContextSize.LOW:
            return low()
        if self is WebSearchOptionsSearchContextSize.MEDIUM:
            return medium()
        if self is WebSearchOptionsSearchContextSize.HIGH:
            return high()
