

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateFulfillOrdersResponseStripeCardBrand(enum.StrEnum):
    """
    The card's brand (ie. credit card network)
    """

    VISA = "Visa"
    AMERICAN_EXPRESS = "American Express"
    MASTER_CARD = "MasterCard"
    DISCOVER = "Discover"
    JCB = "JCB"
    DINERS_CLUB = "Diners Club"
    UNKNOWN = "Unknown"

    def visit(
        self,
        visa: typing.Callable[[], T_Result],
        american_express: typing.Callable[[], T_Result],
        master_card: typing.Callable[[], T_Result],
        discover: typing.Callable[[], T_Result],
        jcb: typing.Callable[[], T_Result],
        diners_club: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UpdateFulfillOrdersResponseStripeCardBrand.VISA:
            return visa()
        if self is UpdateFulfillOrdersResponseStripeCardBrand.AMERICAN_EXPRESS:
            return american_express()
        if self is UpdateFulfillOrdersResponseStripeCardBrand.MASTER_CARD:
            return master_card()
        if self is UpdateFulfillOrdersResponseStripeCardBrand.DISCOVER:
            return discover()
        if self is UpdateFulfillOrdersResponseStripeCardBrand.JCB:
            return jcb()
        if self is UpdateFulfillOrdersResponseStripeCardBrand.DINERS_CLUB:
            return diners_club()
        if self is UpdateFulfillOrdersResponseStripeCardBrand.UNKNOWN:
            return unknown()
