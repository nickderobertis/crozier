

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MarimoDataframeDownloadAsInputFormat(enum.StrEnum):
    CSV = "csv"
    JSON = "json"
    PARQUET = "parquet"
    TSV = "tsv"

    def visit(
        self,
        csv: typing.Callable[[], T_Result],
        json: typing.Callable[[], T_Result],
        parquet: typing.Callable[[], T_Result],
        tsv: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MarimoDataframeDownloadAsInputFormat.CSV:
            return csv()
        if self is MarimoDataframeDownloadAsInputFormat.JSON:
            return json()
        if self is MarimoDataframeDownloadAsInputFormat.PARQUET:
            return parquet()
        if self is MarimoDataframeDownloadAsInputFormat.TSV:
            return tsv()
