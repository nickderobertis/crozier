

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SelectedFulfillmentOptionType(enum.StrEnum):
    SHIPPING = "shipping"
    DIGITAL = "digital"

    def visit(self, shipping: typing.Callable[[], T_Result], digital: typing.Callable[[], T_Result]) -> T_Result:
        if self is SelectedFulfillmentOptionType.SHIPPING:
            return shipping()
        if self is SelectedFulfillmentOptionType.DIGITAL:
            return digital()
