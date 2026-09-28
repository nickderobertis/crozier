

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VisualizeSessionIdGetResponseDataVisualizationsItemContentDataOrientation(enum.StrEnum):
    """
    Chart orientation
    """

    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"

    def visit(self, horizontal: typing.Callable[[], T_Result], vertical: typing.Callable[[], T_Result]) -> T_Result:
        if self is VisualizeSessionIdGetResponseDataVisualizationsItemContentDataOrientation.HORIZONTAL:
            return horizontal()
        if self is VisualizeSessionIdGetResponseDataVisualizationsItemContentDataOrientation.VERTICAL:
            return vertical()
