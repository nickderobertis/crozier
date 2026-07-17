

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostMyNegotiationsIdCounterRequestShippingPriceCurrency(enum.StrEnum):
    """
    The currency the money will be expressed in
    """

    USD = "USD"
    CAD = "CAD"
    EUR = "EUR"
    GBP = "GBP"
    AUD = "AUD"
    JPY = "JPY"
    NZD = "NZD"
    MXN = "MXN"

    def visit(
        self,
        usd: typing.Callable[[], T_Result],
        cad: typing.Callable[[], T_Result],
        eur: typing.Callable[[], T_Result],
        gbp: typing.Callable[[], T_Result],
        aud: typing.Callable[[], T_Result],
        jpy: typing.Callable[[], T_Result],
        nzd: typing.Callable[[], T_Result],
        mxn: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostMyNegotiationsIdCounterRequestShippingPriceCurrency.USD:
            return usd()
        if self is PostMyNegotiationsIdCounterRequestShippingPriceCurrency.CAD:
            return cad()
        if self is PostMyNegotiationsIdCounterRequestShippingPriceCurrency.EUR:
            return eur()
        if self is PostMyNegotiationsIdCounterRequestShippingPriceCurrency.GBP:
            return gbp()
        if self is PostMyNegotiationsIdCounterRequestShippingPriceCurrency.AUD:
            return aud()
        if self is PostMyNegotiationsIdCounterRequestShippingPriceCurrency.JPY:
            return jpy()
        if self is PostMyNegotiationsIdCounterRequestShippingPriceCurrency.NZD:
            return nzd()
        if self is PostMyNegotiationsIdCounterRequestShippingPriceCurrency.MXN:
            return mxn()
