

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class InsightsGetSummaryMetricsWithTrendsRequestReportingWindow(enum.StrEnum):
    LAST7DAYS = "last-7-days"
    LAST90DAYS = "last-90-days"
    LAST24HOURS = "last-24-hours"
    LAST30DAYS = "last-30-days"
    LAST60DAYS = "last-60-days"

    def visit(
        self,
        last7days: typing.Callable[[], T_Result],
        last90days: typing.Callable[[], T_Result],
        last24hours: typing.Callable[[], T_Result],
        last30days: typing.Callable[[], T_Result],
        last60days: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InsightsGetSummaryMetricsWithTrendsRequestReportingWindow.LAST7DAYS:
            return last7days()
        if self is InsightsGetSummaryMetricsWithTrendsRequestReportingWindow.LAST90DAYS:
            return last90days()
        if self is InsightsGetSummaryMetricsWithTrendsRequestReportingWindow.LAST24HOURS:
            return last24hours()
        if self is InsightsGetSummaryMetricsWithTrendsRequestReportingWindow.LAST30DAYS:
            return last30days()
        if self is InsightsGetSummaryMetricsWithTrendsRequestReportingWindow.LAST60DAYS:
            return last60days()
