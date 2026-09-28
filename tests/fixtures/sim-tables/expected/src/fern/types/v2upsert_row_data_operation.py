

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V2UpsertRowDataOperation(enum.StrEnum):
    """
    Whether the row was inserted or updated.
    """

    INSERT = "insert"
    UPDATE = "update"

    def visit(self, insert: typing.Callable[[], T_Result], update: typing.Callable[[], T_Result]) -> T_Result:
        if self is V2UpsertRowDataOperation.INSERT:
            return insert()
        if self is V2UpsertRowDataOperation.UPDATE:
            return update()
