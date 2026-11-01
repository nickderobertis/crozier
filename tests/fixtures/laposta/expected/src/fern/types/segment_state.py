

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SegmentState(enum.StrEnum):
    """
    The state of this segment: active or deleted.
    """

    ACTIVE = "active"
    DELETED = "deleted"

    def visit(self, active: typing.Callable[[], T_Result], deleted: typing.Callable[[], T_Result]) -> T_Result:
        if self is SegmentState.ACTIVE:
            return active()
        if self is SegmentState.DELETED:
            return deleted()
