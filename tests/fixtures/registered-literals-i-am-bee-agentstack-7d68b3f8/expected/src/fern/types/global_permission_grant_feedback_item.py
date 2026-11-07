

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GlobalPermissionGrantFeedbackItem(enum.StrEnum):
    WRITE = "write"

    def visit(self, write: typing.Callable[[], T_Result]) -> T_Result:
        if self is GlobalPermissionGrantFeedbackItem.WRITE:
            return write()
