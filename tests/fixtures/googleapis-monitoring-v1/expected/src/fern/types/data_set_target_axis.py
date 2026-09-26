

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DataSetTargetAxis(enum.StrEnum):
    """
    Optional. The target axis to use for plotting the metric.
    """

    TARGET_AXIS_UNSPECIFIED = "TARGET_AXIS_UNSPECIFIED"
    Y1 = "Y1"
    Y2 = "Y2"

    def visit(
        self,
        target_axis_unspecified: typing.Callable[[], T_Result],
        y1: typing.Callable[[], T_Result],
        y2: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DataSetTargetAxis.TARGET_AXIS_UNSPECIFIED:
            return target_axis_unspecified()
        if self is DataSetTargetAxis.Y1:
            return y1()
        if self is DataSetTargetAxis.Y2:
            return y2()
