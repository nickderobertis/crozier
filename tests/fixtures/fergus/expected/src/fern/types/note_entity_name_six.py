

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NoteEntityNameSix(enum.StrEnum):
    ENQUIRY = "enquiry"

    def visit(self, enquiry: typing.Callable[[], T_Result]) -> T_Result:
        if self is NoteEntityNameSix.ENQUIRY:
            return enquiry()
