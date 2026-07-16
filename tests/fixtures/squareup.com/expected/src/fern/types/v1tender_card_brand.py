

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V1TenderCardBrand(enum.StrEnum):
    """
    The brand of a credit card.
    """

    OTHER_BRAND = "OTHER_BRAND"
    VISA = "VISA"
    MASTER_CARD = "MASTER_CARD"
    AMERICAN_EXPRESS = "AMERICAN_EXPRESS"
    DISCOVER = "DISCOVER"
    DISCOVER_DINERS = "DISCOVER_DINERS"
    JCB = "JCB"
    CHINA_UNIONPAY = "CHINA_UNIONPAY"
    SQUARE_GIFT_CARD = "SQUARE_GIFT_CARD"

    def visit(
        self,
        other_brand: typing.Callable[[], T_Result],
        visa: typing.Callable[[], T_Result],
        master_card: typing.Callable[[], T_Result],
        american_express: typing.Callable[[], T_Result],
        discover: typing.Callable[[], T_Result],
        discover_diners: typing.Callable[[], T_Result],
        jcb: typing.Callable[[], T_Result],
        china_unionpay: typing.Callable[[], T_Result],
        square_gift_card: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V1TenderCardBrand.OTHER_BRAND:
            return other_brand()
        if self is V1TenderCardBrand.VISA:
            return visa()
        if self is V1TenderCardBrand.MASTER_CARD:
            return master_card()
        if self is V1TenderCardBrand.AMERICAN_EXPRESS:
            return american_express()
        if self is V1TenderCardBrand.DISCOVER:
            return discover()
        if self is V1TenderCardBrand.DISCOVER_DINERS:
            return discover_diners()
        if self is V1TenderCardBrand.JCB:
            return jcb()
        if self is V1TenderCardBrand.CHINA_UNIONPAY:
            return china_unionpay()
        if self is V1TenderCardBrand.SQUARE_GIFT_CARD:
            return square_gift_card()
