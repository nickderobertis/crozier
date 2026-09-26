

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SparkChartViewSparkChartType(enum.StrEnum):
    """
    Required. The type of sparkchart to show in this chartView.
    """

    SPARK_CHART_TYPE_UNSPECIFIED = "SPARK_CHART_TYPE_UNSPECIFIED"
    SPARK_LINE = "SPARK_LINE"
    SPARK_BAR = "SPARK_BAR"

    def visit(
        self,
        spark_chart_type_unspecified: typing.Callable[[], T_Result],
        spark_line: typing.Callable[[], T_Result],
        spark_bar: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SparkChartViewSparkChartType.SPARK_CHART_TYPE_UNSPECIFIED:
            return spark_chart_type_unspecified()
        if self is SparkChartViewSparkChartType.SPARK_LINE:
            return spark_line()
        if self is SparkChartViewSparkChartType.SPARK_BAR:
            return spark_bar()
