

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExternalFileNotePartType(enum.StrEnum):
    """
    The type of the note.  Type determines what other fields are present.
    """

    EXTERNAL_FILE = "external_file"

    def visit(self, external_file: typing.Callable[[], T_Result]) -> T_Result:
        if self is ExternalFileNotePartType.EXTERNAL_FILE:
            return external_file()
