

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MixturePrepTableNotePartType(enum.StrEnum):
    """
    The type of the note.  Type determines what other fields are present.
    """

    MIXTURE_PREP_TABLE = "mixture_prep_table"

    def visit(self, mixture_prep_table: typing.Callable[[], T_Result]) -> T_Result:
        if self is MixturePrepTableNotePartType.MIXTURE_PREP_TABLE:
            return mixture_prep_table()
