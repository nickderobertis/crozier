

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VisualizeSessionIdGetResponseDataVisualizationsItemContentDataDataItemStatus(enum.StrEnum):
    """
    Status for color-coding
    """

    ERROR = "error"
    WARNING = "warning"
    OK = "ok"

    def visit(
        self,
        error: typing.Callable[[], T_Result],
        warning: typing.Callable[[], T_Result],
        ok: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VisualizeSessionIdGetResponseDataVisualizationsItemContentDataDataItemStatus.ERROR:
            return error()
        if self is VisualizeSessionIdGetResponseDataVisualizationsItemContentDataDataItemStatus.WARNING:
            return warning()
        if self is VisualizeSessionIdGetResponseDataVisualizationsItemContentDataDataItemStatus.OK:
            return ok()
