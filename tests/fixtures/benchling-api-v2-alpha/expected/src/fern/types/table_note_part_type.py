

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TableNotePartType(enum.StrEnum):
    """
    The type of the note.  Type determines what other fields are present.
    """

    TABLE = "table"

    def visit(self, table: typing.Callable[[], T_Result]) -> T_Result:
        if self is TableNotePartType.TABLE:
            return table()
