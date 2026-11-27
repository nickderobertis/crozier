

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BoxCreationTableNotePartType(enum.StrEnum):
    """
    The type of the note.  Type determines what other fields are present.
    """

    BOX_CREATION_TABLE = "box_creation_table"

    def visit(self, box_creation_table: typing.Callable[[], T_Result]) -> T_Result:
        if self is BoxCreationTableNotePartType.BOX_CREATION_TABLE:
            return box_creation_table()
