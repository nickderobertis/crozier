

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VisualizeSessionIdGetResponseDataVisualizationsItemType(enum.StrEnum):
    """
    Visualization type
    """

    MERMAID = "mermaid"
    CARDS = "cards"
    CODE = "code"
    TABLE = "table"
    DIFF = "diff"
    BAR_CHART = "bar-chart"

    def visit(
        self,
        mermaid: typing.Callable[[], T_Result],
        cards: typing.Callable[[], T_Result],
        code: typing.Callable[[], T_Result],
        table: typing.Callable[[], T_Result],
        diff: typing.Callable[[], T_Result],
        bar_chart: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VisualizeSessionIdGetResponseDataVisualizationsItemType.MERMAID:
            return mermaid()
        if self is VisualizeSessionIdGetResponseDataVisualizationsItemType.CARDS:
            return cards()
        if self is VisualizeSessionIdGetResponseDataVisualizationsItemType.CODE:
            return code()
        if self is VisualizeSessionIdGetResponseDataVisualizationsItemType.TABLE:
            return table()
        if self is VisualizeSessionIdGetResponseDataVisualizationsItemType.DIFF:
            return diff()
        if self is VisualizeSessionIdGetResponseDataVisualizationsItemType.BAR_CHART:
            return bar_chart()
