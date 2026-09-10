

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProductsCreate400DetailsItemARequiredFieldIsMissingIssue(enum.StrEnum):
    MISSING_REQUIRED_PARAMETER = "MISSING_REQUIRED_PARAMETER"

    def visit(self, missing_required_parameter: typing.Callable[[], T_Result]) -> T_Result:
        if self is ProductsCreate400DetailsItemARequiredFieldIsMissingIssue.MISSING_REQUIRED_PARAMETER:
            return missing_required_parameter()
