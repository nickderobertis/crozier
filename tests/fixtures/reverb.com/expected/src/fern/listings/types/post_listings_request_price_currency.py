

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostListingsRequestPriceCurrency(str, enum.Enum):
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
        if self is PostListingsRequestPriceCurrency.USD:
            return usd()
        if self is PostListingsRequestPriceCurrency.CAD:
            return cad()
        if self is PostListingsRequestPriceCurrency.EUR:
            return eur()
        if self is PostListingsRequestPriceCurrency.GBP:
            return gbp()
        if self is PostListingsRequestPriceCurrency.AUD:
            return aud()
        if self is PostListingsRequestPriceCurrency.JPY:
            return jpy()
        if self is PostListingsRequestPriceCurrency.NZD:
            return nzd()
        if self is PostListingsRequestPriceCurrency.MXN:
            return mxn()
