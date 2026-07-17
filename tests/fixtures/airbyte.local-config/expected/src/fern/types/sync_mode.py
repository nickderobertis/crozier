

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SyncMode(enum.StrEnum):
    FULL_REFRESH = "full_refresh"
    INCREMENTAL = "incremental"

    def visit(
        self, full_refresh: typing.Callable[[], T_Result], incremental: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is SyncMode.FULL_REFRESH:
            return full_refresh()
        if self is SyncMode.INCREMENTAL:
            return incremental()
