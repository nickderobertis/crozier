

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CatalogModifierListSelectionType(str, enum.Enum):
    """
    Indicates whether a CatalogModifierList supports multiple selections.
    """

    SINGLE = "SINGLE"
    MULTIPLE = "MULTIPLE"

    def visit(self, single: typing.Callable[[], T_Result], multiple: typing.Callable[[], T_Result]) -> T_Result:
        if self is CatalogModifierListSelectionType.SINGLE:
            return single()
        if self is CatalogModifierListSelectionType.MULTIPLE:
            return multiple()
