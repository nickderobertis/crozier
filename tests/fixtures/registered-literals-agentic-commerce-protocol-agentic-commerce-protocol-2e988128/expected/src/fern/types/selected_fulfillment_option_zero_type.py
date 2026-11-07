

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SelectedFulfillmentOptionZeroType(enum.StrEnum):
    SHIPPING = "shipping"

    def visit(self, shipping: typing.Callable[[], T_Result]) -> T_Result:
        if self is SelectedFulfillmentOptionZeroType.SHIPPING:
            return shipping()
