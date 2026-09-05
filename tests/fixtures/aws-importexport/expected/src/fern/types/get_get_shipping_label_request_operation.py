

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetGetShippingLabelRequestOperation(enum.StrEnum):
    GET_SHIPPING_LABEL = "GetShippingLabel"

    def visit(self, get_shipping_label: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetGetShippingLabelRequestOperation.GET_SHIPPING_LABEL:
            return get_shipping_label()
