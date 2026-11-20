

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StudioNoteType(enum.StrEnum):
    NOTE = "note"

    def visit(self, note: typing.Callable[[], T_Result]) -> T_Result:
        if self is StudioNoteType.NOTE:
            return note()
