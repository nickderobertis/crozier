

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProductsPatch422DetailsItemDuplicateResourceIdentifierDescription(enum.StrEnum):
    IDENTIFIER_MUST_BE_UNIQUE = "Identifier must be unique."

    def visit(self, identifier_must_be_unique: typing.Callable[[], T_Result]) -> T_Result:
        if self is ProductsPatch422DetailsItemDuplicateResourceIdentifierDescription.IDENTIFIER_MUST_BE_UNIQUE:
            return identifier_must_be_unique()
