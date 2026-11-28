

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CheckboxNotePartType(enum.StrEnum):
    """
    The type of the note.  Type determines what other fields are present.
    """

    LIST_CHECKBOX = "list_checkbox"

    def visit(self, list_checkbox: typing.Callable[[], T_Result]) -> T_Result:
        if self is CheckboxNotePartType.LIST_CHECKBOX:
            return list_checkbox()
