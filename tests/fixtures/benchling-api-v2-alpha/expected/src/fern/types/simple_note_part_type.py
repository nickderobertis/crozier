

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SimpleNotePartType(enum.StrEnum):
    """
    The type of the note.  Type determines what other fields are present.
    """

    TEXT = "text"
    CODE = "code"
    LIST_BULLET = "list_bullet"
    LIST_NUMBER = "list_number"

    def visit(
        self,
        text: typing.Callable[[], T_Result],
        code: typing.Callable[[], T_Result],
        list_bullet: typing.Callable[[], T_Result],
        list_number: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SimpleNotePartType.TEXT:
            return text()
        if self is SimpleNotePartType.CODE:
            return code()
        if self is SimpleNotePartType.LIST_BULLET:
            return list_bullet()
        if self is SimpleNotePartType.LIST_NUMBER:
            return list_number()
