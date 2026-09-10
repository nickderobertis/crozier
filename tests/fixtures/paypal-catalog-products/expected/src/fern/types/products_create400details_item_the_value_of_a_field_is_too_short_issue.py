

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProductsCreate400DetailsItemTheValueOfAFieldIsTooShortIssue(enum.StrEnum):
    INVALID_STRING_MIN_LENGTH = "INVALID_STRING_MIN_LENGTH"

    def visit(self, invalid_string_min_length: typing.Callable[[], T_Result]) -> T_Result:
        if self is ProductsCreate400DetailsItemTheValueOfAFieldIsTooShortIssue.INVALID_STRING_MIN_LENGTH:
            return invalid_string_min_length()
