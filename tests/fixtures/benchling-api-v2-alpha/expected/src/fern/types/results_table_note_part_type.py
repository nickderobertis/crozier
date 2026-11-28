

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResultsTableNotePartType(enum.StrEnum):
    """
    The type of the note.  Type determines what other fields are present.
    """

    RESULTS_TABLE = "results_table"

    def visit(self, results_table: typing.Callable[[], T_Result]) -> T_Result:
        if self is ResultsTableNotePartType.RESULTS_TABLE:
            return results_table()
