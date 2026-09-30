

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MssqlSourceMetadataKind(enum.StrEnum):
    MSSQL = "mssql"

    def visit(self, mssql: typing.Callable[[], T_Result]) -> T_Result:
        if self is MssqlSourceMetadataKind.MSSQL:
            return mssql()
