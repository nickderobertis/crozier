

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class QuoteSectionsItemSelectionMode(enum.StrEnum):
    FIXED = "Fixed"
    OPTIONAL = "Optional"
    MULTIPLE_CHOICE = "Multiple Choice"

    def visit(
        self,
        fixed: typing.Callable[[], T_Result],
        optional: typing.Callable[[], T_Result],
        multiple_choice: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is QuoteSectionsItemSelectionMode.FIXED:
            return fixed()
        if self is QuoteSectionsItemSelectionMode.OPTIONAL:
            return optional()
        if self is QuoteSectionsItemSelectionMode.MULTIPLE_CHOICE:
            return multiple_choice()
