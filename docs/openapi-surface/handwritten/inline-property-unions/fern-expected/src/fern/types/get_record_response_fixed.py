

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetRecordResponseFixed(enum.StrEnum):
    """
    annotated
    """

    FIXED = "fixed"

    def visit(self, fixed: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetRecordResponseFixed.FIXED:
            return fixed()
