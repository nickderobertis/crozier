

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V2TableExportFormat(enum.StrEnum):
    """
    Export file format.
    """

    CSV = "csv"
    JSON = "json"

    def visit(self, csv: typing.Callable[[], T_Result], json: typing.Callable[[], T_Result]) -> T_Result:
        if self is V2TableExportFormat.CSV:
            return csv()
        if self is V2TableExportFormat.JSON:
            return json()
