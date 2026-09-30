

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostgresSourceMetadataKind(enum.StrEnum):
    POSTGRES = "postgres"
    PG = "pg"

    def visit(self, postgres: typing.Callable[[], T_Result], pg: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostgresSourceMetadataKind.POSTGRES:
            return postgres()
        if self is PostgresSourceMetadataKind.PG:
            return pg()
