

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostMyNegotiationsIdCounterRequestPriceCurrency(str, enum.Enum):
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
        if self is PostMyNegotiationsIdCounterRequestPriceCurrency.USD:
            return usd()
        if self is PostMyNegotiationsIdCounterRequestPriceCurrency.CAD:
            return cad()
        if self is PostMyNegotiationsIdCounterRequestPriceCurrency.EUR:
            return eur()
        if self is PostMyNegotiationsIdCounterRequestPriceCurrency.GBP:
            return gbp()
        if self is PostMyNegotiationsIdCounterRequestPriceCurrency.AUD:
            return aud()
        if self is PostMyNegotiationsIdCounterRequestPriceCurrency.JPY:
            return jpy()
        if self is PostMyNegotiationsIdCounterRequestPriceCurrency.NZD:
            return nzd()
        if self is PostMyNegotiationsIdCounterRequestPriceCurrency.MXN:
            return mxn()
