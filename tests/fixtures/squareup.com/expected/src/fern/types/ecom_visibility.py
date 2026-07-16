

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EcomVisibility(str, enum.Enum):
    """
    Determines item visibility in Ecom (Online Store) and Online Checkout.
    """

    UNINDEXED = "UNINDEXED"
    UNAVAILABLE = "UNAVAILABLE"
    HIDDEN = "HIDDEN"
    VISIBLE = "VISIBLE"

    def visit(
        self,
        unindexed: typing.Callable[[], T_Result],
        unavailable: typing.Callable[[], T_Result],
        hidden: typing.Callable[[], T_Result],
        visible: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EcomVisibility.UNINDEXED:
            return unindexed()
        if self is EcomVisibility.UNAVAILABLE:
            return unavailable()
        if self is EcomVisibility.HIDDEN:
            return hidden()
        if self is EcomVisibility.VISIBLE:
            return visible()
