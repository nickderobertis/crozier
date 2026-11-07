

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ItemReferenceParamType(enum.StrEnum):
    """
    The type of item to reference. Always `item_reference`.
    """

    ITEM_REFERENCE = "item_reference"

    def visit(self, item_reference: typing.Callable[[], T_Result]) -> T_Result:
        if self is ItemReferenceParamType.ITEM_REFERENCE:
            return item_reference()
