

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TextBoxNotePartType(enum.StrEnum):
    """
    The type of the note.  Type determines what other fields are present.
    """

    TEXT_BOX = "text_box"

    def visit(self, text_box: typing.Callable[[], T_Result]) -> T_Result:
        if self is TextBoxNotePartType.TEXT_BOX:
            return text_box()
