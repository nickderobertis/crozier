

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProjectAutomationConfigBtqlExportFormat(enum.StrEnum):
    """
    The format to export the results in
    """

    JSONL = "jsonl"
    PARQUET = "parquet"

    def visit(self, jsonl: typing.Callable[[], T_Result], parquet: typing.Callable[[], T_Result]) -> T_Result:
        if self is ProjectAutomationConfigBtqlExportFormat.JSONL:
            return jsonl()
        if self is ProjectAutomationConfigBtqlExportFormat.PARQUET:
            return parquet()
