

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SplitViewAlertType(enum.StrEnum):
    SPLIT_VIEW_DETECTED = "split_view_detected"

    def visit(self, split_view_detected: typing.Callable[[], T_Result]) -> T_Result:
        if self is SplitViewAlertType.SPLIT_VIEW_DETECTED:
            return split_view_detected()
