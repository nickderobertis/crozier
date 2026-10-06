

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RenderMode(enum.StrEnum):
    """
    Render mode configuration keys.
    """

    HEADER_ROW = "HEADER_ROW"
    COMPACT = "COMPACT"
    SERIES = "SERIES"
    HEADER_COLUMN = "HEADER_COLUMN"
    FLAT_DICT = "FLAT_DICT"
    HIER_DICT = "HIER_DICT"
    METRIC_FLAT_DICT = "METRIC_FLAT_DICT"
    UPLOAD = "UPLOAD"
    COMPACT_WS = "COMPACT_WS"
    CSV = "CSV"

    def visit(
        self,
        header_row: typing.Callable[[], T_Result],
        compact: typing.Callable[[], T_Result],
        series: typing.Callable[[], T_Result],
        header_column: typing.Callable[[], T_Result],
        flat_dict: typing.Callable[[], T_Result],
        hier_dict: typing.Callable[[], T_Result],
        metric_flat_dict: typing.Callable[[], T_Result],
        upload: typing.Callable[[], T_Result],
        compact_ws: typing.Callable[[], T_Result],
        csv: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RenderMode.HEADER_ROW:
            return header_row()
        if self is RenderMode.COMPACT:
            return compact()
        if self is RenderMode.SERIES:
            return series()
        if self is RenderMode.HEADER_COLUMN:
            return header_column()
        if self is RenderMode.FLAT_DICT:
            return flat_dict()
        if self is RenderMode.HIER_DICT:
            return hier_dict()
        if self is RenderMode.METRIC_FLAT_DICT:
            return metric_flat_dict()
        if self is RenderMode.UPLOAD:
            return upload()
        if self is RenderMode.COMPACT_WS:
            return compact_ws()
        if self is RenderMode.CSV:
            return csv()
