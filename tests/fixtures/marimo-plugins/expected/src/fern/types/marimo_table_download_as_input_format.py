

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MarimoTableDownloadAsInputFormat(enum.StrEnum):
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
        if self is MarimoTableDownloadAsInputFormat.CSV:
            return csv()
        if self is MarimoTableDownloadAsInputFormat.JSON:
            return json()
        if self is MarimoTableDownloadAsInputFormat.PARQUET:
            return parquet()
        if self is MarimoTableDownloadAsInputFormat.TSV:
            return tsv()
