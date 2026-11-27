

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RegistrationTableNotePartType(enum.StrEnum):
    """
    The type of the note.  Type determines what other fields are present.
    """

    REGISTRATION_TABLE = "registration_table"

    def visit(self, registration_table: typing.Callable[[], T_Result]) -> T_Result:
        if self is RegistrationTableNotePartType.REGISTRATION_TABLE:
            return registration_table()
