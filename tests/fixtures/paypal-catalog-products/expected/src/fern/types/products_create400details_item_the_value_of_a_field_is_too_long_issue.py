

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProductsCreate400DetailsItemTheValueOfAFieldIsTooLongIssue(enum.StrEnum):
    INVALID_STRING_MAX_LENGTH = "INVALID_STRING_MAX_LENGTH"

    def visit(self, invalid_string_max_length: typing.Callable[[], T_Result]) -> T_Result:
        if self is ProductsCreate400DetailsItemTheValueOfAFieldIsTooLongIssue.INVALID_STRING_MAX_LENGTH:
            return invalid_string_max_length()
