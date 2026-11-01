

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MovePageParentRequestDatabaseIdType(enum.StrEnum):
    DATABASE_ID = "database_id"

    def visit(self, database_id: typing.Callable[[], T_Result]) -> T_Result:
        if self is MovePageParentRequestDatabaseIdType.DATABASE_ID:
            return database_id()
