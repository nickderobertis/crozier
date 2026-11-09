

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CardBrand(enum.StrEnum):
    AMEX = "amex"
    CARTES_BANCAIRES = "cartes_bancaires"
    DINERS = "diners"
    DISCOVER = "discover"
    JCB = "jcb"
    MASTERCARD = "mastercard"
    VISA = "visa"
    UNIONPAY = "unionpay"
    CARD = "card"

    def visit(
        self,
        amex: typing.Callable[[], T_Result],
        cartes_bancaires: typing.Callable[[], T_Result],
        diners: typing.Callable[[], T_Result],
        discover: typing.Callable[[], T_Result],
        jcb: typing.Callable[[], T_Result],
        mastercard: typing.Callable[[], T_Result],
        visa: typing.Callable[[], T_Result],
        unionpay: typing.Callable[[], T_Result],
        card: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CardBrand.AMEX:
            return amex()
        if self is CardBrand.CARTES_BANCAIRES:
            return cartes_bancaires()
        if self is CardBrand.DINERS:
            return diners()
        if self is CardBrand.DISCOVER:
            return discover()
        if self is CardBrand.JCB:
            return jcb()
        if self is CardBrand.MASTERCARD:
            return mastercard()
        if self is CardBrand.VISA:
            return visa()
        if self is CardBrand.UNIONPAY:
            return unionpay()
        if self is CardBrand.CARD:
            return card()
