

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetQuoteByIdQuoteResponseDataSectionsItemSelectionMode(enum.StrEnum):
    FIXED = "Fixed"
    OPTIONAL = "Optional"
    MULTIPLE_CHOICE = "Multiple Choice"

    def visit(
        self,
        fixed: typing.Callable[[], T_Result],
        optional: typing.Callable[[], T_Result],
        multiple_choice: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetQuoteByIdQuoteResponseDataSectionsItemSelectionMode.FIXED:
            return fixed()
        if self is GetQuoteByIdQuoteResponseDataSectionsItemSelectionMode.OPTIONAL:
            return optional()
        if self is GetQuoteByIdQuoteResponseDataSectionsItemSelectionMode.MULTIPLE_CHOICE:
            return multiple_choice()
