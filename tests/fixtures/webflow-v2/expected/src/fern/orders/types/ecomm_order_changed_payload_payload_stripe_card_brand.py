

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class EcommOrderChangedPayloadPayloadStripeCardBrand(enum.StrEnum):
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
        if self is EcommOrderChangedPayloadPayloadStripeCardBrand.VISA:
            return visa()
        if self is EcommOrderChangedPayloadPayloadStripeCardBrand.AMERICAN_EXPRESS:
            return american_express()
        if self is EcommOrderChangedPayloadPayloadStripeCardBrand.MASTER_CARD:
            return master_card()
        if self is EcommOrderChangedPayloadPayloadStripeCardBrand.DISCOVER:
            return discover()
        if self is EcommOrderChangedPayloadPayloadStripeCardBrand.JCB:
            return jcb()
        if self is EcommOrderChangedPayloadPayloadStripeCardBrand.DINERS_CLUB:
            return diners_club()
        if self is EcommOrderChangedPayloadPayloadStripeCardBrand.UNKNOWN:
            return unknown()
