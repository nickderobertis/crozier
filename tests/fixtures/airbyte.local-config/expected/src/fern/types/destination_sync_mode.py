

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DestinationSyncMode(enum.StrEnum):
    APPEND = "append"
    OVERWRITE = "overwrite"
    APPEND_DEDUP = "append_dedup"

    def visit(
        self,
        append: typing.Callable[[], T_Result],
        overwrite: typing.Callable[[], T_Result],
        append_dedup: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DestinationSyncMode.APPEND:
            return append()
        if self is DestinationSyncMode.OVERWRITE:
            return overwrite()
        if self is DestinationSyncMode.APPEND_DEDUP:
            return append_dedup()
