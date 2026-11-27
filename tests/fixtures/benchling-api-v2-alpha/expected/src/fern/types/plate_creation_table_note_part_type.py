

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PlateCreationTableNotePartType(enum.StrEnum):
    """
    The type of the note.  Type determines what other fields are present.
    """

    PLATE_CREATION_TABLE = "plate_creation_table"

    def visit(self, plate_creation_table: typing.Callable[[], T_Result]) -> T_Result:
        if self is PlateCreationTableNotePartType.PLATE_CREATION_TABLE:
            return plate_creation_table()
