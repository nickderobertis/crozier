

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostGetShippingLabelRequestAction(enum.StrEnum):
    GET_SHIPPING_LABEL = "GetShippingLabel"

    def visit(self, get_shipping_label: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostGetShippingLabelRequestAction.GET_SHIPPING_LABEL:
            return get_shipping_label()
