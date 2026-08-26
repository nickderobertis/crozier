

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DataTableSourceType(enum.StrEnum):
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
        if self is DataTableSourceType.CATALOG:
            return catalog()
        if self is DataTableSourceType.CONNECTION:
            return connection()
        if self is DataTableSourceType.DUCKDB:
            return duckdb()
        if self is DataTableSourceType.LOCAL:
            return local()
