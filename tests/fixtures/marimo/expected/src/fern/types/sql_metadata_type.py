

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SqlMetadataType(enum.StrEnum):
    SQL_METADATA = "sql-metadata"

    def visit(self, sql_metadata: typing.Callable[[], T_Result]) -> T_Result:
        if self is SqlMetadataType.SQL_METADATA:
            return sql_metadata()
