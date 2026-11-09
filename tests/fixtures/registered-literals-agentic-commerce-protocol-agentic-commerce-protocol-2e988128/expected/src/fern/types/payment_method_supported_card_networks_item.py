

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PaymentMethodSupportedCardNetworksItem(enum.StrEnum):
    AMEX = "amex"
    DISCOVER = "discover"
    MASTERCARD = "mastercard"
    VISA = "visa"

    def visit(
        self,
        amex: typing.Callable[[], T_Result],
        discover: typing.Callable[[], T_Result],
        mastercard: typing.Callable[[], T_Result],
        visa: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PaymentMethodSupportedCardNetworksItem.AMEX:
            return amex()
        if self is PaymentMethodSupportedCardNetworksItem.DISCOVER:
            return discover()
        if self is PaymentMethodSupportedCardNetworksItem.MASTERCARD:
            return mastercard()
        if self is PaymentMethodSupportedCardNetworksItem.VISA:
            return visa()
