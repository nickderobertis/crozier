

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class QaMetaConformance(enum.StrEnum):
    """
    Conformance level of the record.
    """

    COMPLETE = "complete"
    USEFUL = "useful"
    VALID = "valid"

    def visit(
        self,
        complete: typing.Callable[[], T_Result],
        useful: typing.Callable[[], T_Result],
        valid: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is QaMetaConformance.COMPLETE:
            return complete()
        if self is QaMetaConformance.USEFUL:
            return useful()
        if self is QaMetaConformance.VALID:
            return valid()
