

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DatasetsNotificationClearChannel(enum.StrEnum):
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
        if self is DatasetsNotificationClearChannel.CATALOG:
            return catalog()
        if self is DatasetsNotificationClearChannel.CONNECTION:
            return connection()
        if self is DatasetsNotificationClearChannel.DUCKDB:
            return duckdb()
        if self is DatasetsNotificationClearChannel.LOCAL:
            return local()
