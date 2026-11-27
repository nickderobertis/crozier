

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AssayRunNotePartType(enum.StrEnum):
    """
    The type of the note.  Type determines what other fields are present.
    """

    ASSAY_RUN = "assay_run"

    def visit(self, assay_run: typing.Callable[[], T_Result]) -> T_Result:
        if self is AssayRunNotePartType.ASSAY_RUN:
            return assay_run()
