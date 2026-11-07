

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DestinationStripeConfigObject(enum.StrEnum):
    CUSTOM_OBJECT = "custom_object"

    def visit(self, custom_object: typing.Callable[[], T_Result]) -> T_Result:
        if self is DestinationStripeConfigObject.CUSTOM_OBJECT:
            return custom_object()
