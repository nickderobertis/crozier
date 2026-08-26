

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PreviewDatasetColumnCommandSourceType(enum.StrEnum):
    CATALOG = "catalog"
    CONNECTION = "connection"
    DUCKDB = "duckdb"
    LOCAL = "local"

    def visit(
        self,
        catalog: typing.Callable[[], T_Result],
        connection: typing.Callable[[], T_Result],
        duckdb: typing.Callable[[], T_Result],
        local: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PreviewDatasetColumnCommandSourceType.CATALOG:
            return catalog()
        if self is PreviewDatasetColumnCommandSourceType.CONNECTION:
            return connection()
        if self is PreviewDatasetColumnCommandSourceType.DUCKDB:
            return duckdb()
        if self is PreviewDatasetColumnCommandSourceType.LOCAL:
            return local()
