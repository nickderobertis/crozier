

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AddQuoteResponseDataSectionsItemSelectionMode(enum.StrEnum):
    FIXED = "Fixed"
    OPTIONAL = "Optional"
    MULTIPLE_CHOICE = "Multiple Choice"

    def visit(
        self,
        fixed: typing.Callable[[], T_Result],
        optional: typing.Callable[[], T_Result],
        multiple_choice: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AddQuoteResponseDataSectionsItemSelectionMode.FIXED:
            return fixed()
        if self is AddQuoteResponseDataSectionsItemSelectionMode.OPTIONAL:
            return optional()
        if self is AddQuoteResponseDataSectionsItemSelectionMode.MULTIPLE_CHOICE:
            return multiple_choice()
