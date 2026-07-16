

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetListTypeVersionsRequestDeprecatedStatus(enum.StrEnum):
    LIVE = "LIVE"
    DEPRECATED = "DEPRECATED"

    def visit(self, live: typing.Callable[[], T_Result], deprecated: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetListTypeVersionsRequestDeprecatedStatus.LIVE:
            return live()
        if self is GetListTypeVersionsRequestDeprecatedStatus.DEPRECATED:
            return deprecated()
