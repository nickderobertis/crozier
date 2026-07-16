

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DeprecatedStatus(enum.StrEnum):
    LIVE = "LIVE"
    DEPRECATED = "DEPRECATED"

    def visit(self, live: typing.Callable[[], T_Result], deprecated: typing.Callable[[], T_Result]) -> T_Result:
        if self is DeprecatedStatus.LIVE:
            return live()
        if self is DeprecatedStatus.DEPRECATED:
            return deprecated()
