

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetV1ShapeResponseZeroItemHeadersControl(enum.StrEnum):
    UP_TO_DATE = "up-to-date"
    MUST_REFETCH = "must-refetch"
    SNAPSHOT_END = "snapshot-end"

    def visit(
        self,
        up_to_date: typing.Callable[[], T_Result],
        must_refetch: typing.Callable[[], T_Result],
        snapshot_end: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetV1ShapeResponseZeroItemHeadersControl.UP_TO_DATE:
            return up_to_date()
        if self is GetV1ShapeResponseZeroItemHeadersControl.MUST_REFETCH:
            return must_refetch()
        if self is GetV1ShapeResponseZeroItemHeadersControl.SNAPSHOT_END:
            return snapshot_end()
