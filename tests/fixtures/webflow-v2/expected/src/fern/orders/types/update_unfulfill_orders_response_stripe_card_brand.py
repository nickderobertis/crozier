

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateUnfulfillOrdersResponseStripeCardBrand(enum.StrEnum):
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
        if self is UpdateUnfulfillOrdersResponseStripeCardBrand.VISA:
            return visa()
        if self is UpdateUnfulfillOrdersResponseStripeCardBrand.AMERICAN_EXPRESS:
            return american_express()
        if self is UpdateUnfulfillOrdersResponseStripeCardBrand.MASTER_CARD:
            return master_card()
        if self is UpdateUnfulfillOrdersResponseStripeCardBrand.DISCOVER:
            return discover()
        if self is UpdateUnfulfillOrdersResponseStripeCardBrand.JCB:
            return jcb()
        if self is UpdateUnfulfillOrdersResponseStripeCardBrand.DINERS_CLUB:
            return diners_club()
        if self is UpdateUnfulfillOrdersResponseStripeCardBrand.UNKNOWN:
            return unknown()
