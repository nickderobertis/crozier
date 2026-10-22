

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SyncStrategy(enum.StrEnum):
    FAST_SYNC = "FastSync"
    FULL_SYNC = "FullSync"
    FULL_SCAN = "FullScan"

    def visit(
        self,
        fast_sync: typing.Callable[[], T_Result],
        full_sync: typing.Callable[[], T_Result],
        full_scan: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SyncStrategy.FAST_SYNC:
            return fast_sync()
        if self is SyncStrategy.FULL_SYNC:
            return full_sync()
        if self is SyncStrategy.FULL_SCAN:
            return full_scan()
