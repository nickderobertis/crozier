

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PreviewDatasetColumnRequestSourceType(enum.StrEnum):
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
        if self is PreviewDatasetColumnRequestSourceType.CATALOG:
            return catalog()
        if self is PreviewDatasetColumnRequestSourceType.CONNECTION:
            return connection()
        if self is PreviewDatasetColumnRequestSourceType.DUCKDB:
            return duckdb()
        if self is PreviewDatasetColumnRequestSourceType.LOCAL:
            return local()
