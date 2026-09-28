

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PieChartChartType(enum.StrEnum):
    """
    Required. Indicates the visualization type for the PieChart.
    """

    PIE_CHART_TYPE_UNSPECIFIED = "PIE_CHART_TYPE_UNSPECIFIED"
    PIE = "PIE"
    DONUT = "DONUT"

    def visit(
        self,
        pie_chart_type_unspecified: typing.Callable[[], T_Result],
        pie: typing.Callable[[], T_Result],
        donut: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PieChartChartType.PIE_CHART_TYPE_UNSPECIFIED:
            return pie_chart_type_unspecified()
        if self is PieChartChartType.PIE:
            return pie()
        if self is PieChartChartType.DONUT:
            return donut()
