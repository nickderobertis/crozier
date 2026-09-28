

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DataSetPlotType(enum.StrEnum):
    """
    How this data should be plotted on the chart.
    """

    PLOT_TYPE_UNSPECIFIED = "PLOT_TYPE_UNSPECIFIED"
    LINE = "LINE"
    STACKED_AREA = "STACKED_AREA"
    STACKED_BAR = "STACKED_BAR"
    HEATMAP = "HEATMAP"

    def visit(
        self,
        plot_type_unspecified: typing.Callable[[], T_Result],
        line: typing.Callable[[], T_Result],
        stacked_area: typing.Callable[[], T_Result],
        stacked_bar: typing.Callable[[], T_Result],
        heatmap: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DataSetPlotType.PLOT_TYPE_UNSPECIFIED:
            return plot_type_unspecified()
        if self is DataSetPlotType.LINE:
            return line()
        if self is DataSetPlotType.STACKED_AREA:
            return stacked_area()
        if self is DataSetPlotType.STACKED_BAR:
            return stacked_bar()
        if self is DataSetPlotType.HEATMAP:
            return heatmap()
