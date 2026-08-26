

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListDataSourceConnectionCommandType(enum.StrEnum):
    LIST_DATA_SOURCE_CONNECTION = "list-data-source-connection"

    def visit(self, list_data_source_connection: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListDataSourceConnectionCommandType.LIST_DATA_SOURCE_CONNECTION:
            return list_data_source_connection()
