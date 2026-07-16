

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CardBrand(str, enum.Enum):
    """
    Indicates a card's brand, such as `VISA` or `MASTERCARD`.
    """

    OTHER_BRAND = "OTHER_BRAND"
    VISA = "VISA"
    MASTERCARD = "MASTERCARD"
    AMERICAN_EXPRESS = "AMERICAN_EXPRESS"
    DISCOVER = "DISCOVER"
    DISCOVER_DINERS = "DISCOVER_DINERS"
    JCB = "JCB"
    CHINA_UNIONPAY = "CHINA_UNIONPAY"
    SQUARE_GIFT_CARD = "SQUARE_GIFT_CARD"
    SQUARE_CAPITAL_CARD = "SQUARE_CAPITAL_CARD"
    INTERAC = "INTERAC"
    EFTPOS = "EFTPOS"
    FELICA = "FELICA"
    EBT = "EBT"

    def visit(
        self,
        other_brand: typing.Callable[[], T_Result],
        visa: typing.Callable[[], T_Result],
        mastercard: typing.Callable[[], T_Result],
        american_express: typing.Callable[[], T_Result],
        discover: typing.Callable[[], T_Result],
        discover_diners: typing.Callable[[], T_Result],
        jcb: typing.Callable[[], T_Result],
        china_unionpay: typing.Callable[[], T_Result],
        square_gift_card: typing.Callable[[], T_Result],
        square_capital_card: typing.Callable[[], T_Result],
        interac: typing.Callable[[], T_Result],
        eftpos: typing.Callable[[], T_Result],
        felica: typing.Callable[[], T_Result],
        ebt: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CardBrand.OTHER_BRAND:
            return other_brand()
        if self is CardBrand.VISA:
            return visa()
        if self is CardBrand.MASTERCARD:
            return mastercard()
        if self is CardBrand.AMERICAN_EXPRESS:
            return american_express()
        if self is CardBrand.DISCOVER:
            return discover()
        if self is CardBrand.DISCOVER_DINERS:
            return discover_diners()
        if self is CardBrand.JCB:
            return jcb()
        if self is CardBrand.CHINA_UNIONPAY:
            return china_unionpay()
        if self is CardBrand.SQUARE_GIFT_CARD:
            return square_gift_card()
        if self is CardBrand.SQUARE_CAPITAL_CARD:
            return square_capital_card()
        if self is CardBrand.INTERAC:
            return interac()
        if self is CardBrand.EFTPOS:
            return eftpos()
        if self is CardBrand.FELICA:
            return felica()
        if self is CardBrand.EBT:
            return ebt()
