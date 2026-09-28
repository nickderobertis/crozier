

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChartOptionsMode(enum.StrEnum):
    """
    The chart mode.
    """

    MODE_UNSPECIFIED = "MODE_UNSPECIFIED"
    COLOR = "COLOR"
    X_RAY = "X_RAY"
    STATS = "STATS"

    def visit(
        self,
        mode_unspecified: typing.Callable[[], T_Result],
        color: typing.Callable[[], T_Result],
        x_ray: typing.Callable[[], T_Result],
        stats: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChartOptionsMode.MODE_UNSPECIFIED:
            return mode_unspecified()
        if self is ChartOptionsMode.COLOR:
            return color()
        if self is ChartOptionsMode.X_RAY:
            return x_ray()
        if self is ChartOptionsMode.STATS:
            return stats()
