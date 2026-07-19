

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetV1ShapeRequestLog(enum.StrEnum):
    FULL = "full"
    CHANGES_ONLY = "changes_only"

    def visit(self, full: typing.Callable[[], T_Result], changes_only: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetV1ShapeRequestLog.FULL:
            return full()
        if self is GetV1ShapeRequestLog.CHANGES_ONLY:
            return changes_only()
