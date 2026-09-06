

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class EcommOrderChangedPayloadPayloadShippingAddressType(enum.StrEnum):
    """
    The type of the order address (billing or shipping)
    """

    SHIPPING = "shipping"
    BILLING = "billing"

    def visit(self, shipping: typing.Callable[[], T_Result], billing: typing.Callable[[], T_Result]) -> T_Result:
        if self is EcommOrderChangedPayloadPayloadShippingAddressType.SHIPPING:
            return shipping()
        if self is EcommOrderChangedPayloadPayloadShippingAddressType.BILLING:
            return billing()
