

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DataSourceConnectionsNotificationOp(enum.StrEnum):
    DATA_SOURCE_CONNECTIONS = "data-source-connections"

    def visit(self, data_source_connections: typing.Callable[[], T_Result]) -> T_Result:
        if self is DataSourceConnectionsNotificationOp.DATA_SOURCE_CONNECTIONS:
            return data_source_connections()
