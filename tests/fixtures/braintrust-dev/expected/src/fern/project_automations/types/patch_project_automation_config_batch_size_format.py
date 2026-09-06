

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PatchProjectAutomationConfigBatchSizeFormat(enum.StrEnum):
    """
    The format to export the results in
    """

    JSONL = "jsonl"
    PARQUET = "parquet"

    def visit(self, jsonl: typing.Callable[[], T_Result], parquet: typing.Callable[[], T_Result]) -> T_Result:
        if self is PatchProjectAutomationConfigBatchSizeFormat.JSONL:
            return jsonl()
        if self is PatchProjectAutomationConfigBatchSizeFormat.PARQUET:
            return parquet()
