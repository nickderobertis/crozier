

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LineageConfidenceAssertionKind(enum.StrEnum):
    REPORTED = "reported"
    DERIVED = "derived"
    ASSESSED = "assessed"

    def visit(
        self,
        reported: typing.Callable[[], T_Result],
        derived: typing.Callable[[], T_Result],
        assessed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LineageConfidenceAssertionKind.REPORTED:
            return reported()
        if self is LineageConfidenceAssertionKind.DERIVED:
            return derived()
        if self is LineageConfidenceAssertionKind.ASSESSED:
            return assessed()
