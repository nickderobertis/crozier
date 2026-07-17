

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PutShopRequestCurrency(enum.StrEnum):
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
        if self is PutShopRequestCurrency.USD:
            return usd()
        if self is PutShopRequestCurrency.CAD:
            return cad()
        if self is PutShopRequestCurrency.EUR:
            return eur()
        if self is PutShopRequestCurrency.GBP:
            return gbp()
        if self is PutShopRequestCurrency.AUD:
            return aud()
        if self is PutShopRequestCurrency.JPY:
            return jpy()
        if self is PutShopRequestCurrency.NZD:
            return nzd()
        if self is PutShopRequestCurrency.MXN:
            return mxn()
