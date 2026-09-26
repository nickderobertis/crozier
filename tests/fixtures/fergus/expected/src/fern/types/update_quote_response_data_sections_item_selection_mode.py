

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateQuoteResponseDataSectionsItemSelectionMode(enum.StrEnum):
    FIXED = "Fixed"
    OPTIONAL = "Optional"
    MULTIPLE_CHOICE = "Multiple Choice"

    def visit(
        self,
        fixed: typing.Callable[[], T_Result],
        optional: typing.Callable[[], T_Result],
        multiple_choice: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UpdateQuoteResponseDataSectionsItemSelectionMode.FIXED:
            return fixed()
        if self is UpdateQuoteResponseDataSectionsItemSelectionMode.OPTIONAL:
            return optional()
        if self is UpdateQuoteResponseDataSectionsItemSelectionMode.MULTIPLE_CHOICE:
            return multiple_choice()
