

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NoteEntityNameThree(enum.StrEnum):
    QUOTE = "quote"

    def visit(self, quote: typing.Callable[[], T_Result]) -> T_Result:
        if self is NoteEntityNameThree.QUOTE:
            return quote()
