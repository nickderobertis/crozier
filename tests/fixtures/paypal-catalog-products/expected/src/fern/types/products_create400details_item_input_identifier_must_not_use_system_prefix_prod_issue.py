

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProductsCreate400DetailsItemInputIdentifierMustNotUseSystemPrefixProdIssue(enum.StrEnum):
    INVALID_PARAMETER_SYNTAX = "INVALID_PARAMETER_SYNTAX"

    def visit(self, invalid_parameter_syntax: typing.Callable[[], T_Result]) -> T_Result:
        if self is ProductsCreate400DetailsItemInputIdentifierMustNotUseSystemPrefixProdIssue.INVALID_PARAMETER_SYNTAX:
            return invalid_parameter_syntax()
