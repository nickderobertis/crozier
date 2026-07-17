

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostMyFollowsSearchRequestCurrency(enum.StrEnum):
    """
    The currency to be used for the price filters
    """

    USD = "USD"
    CAD = "CAD"
    EUR = "EUR"
    GBP = "GBP"
    AUD = "AUD"
    JPY = "JPY"
    NZD = "NZD"
    MXN = "MXN"
    DKK = "DKK"
    SEK = "SEK"
    CHF = "CHF"
    ARS = "ARS"
    BRL = "BRL"
    HKD = "HKD"
    NOK = "NOK"
    PHP = "PHP"
    PLN = "PLN"
    RUB = "RUB"

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
        dkk: typing.Callable[[], T_Result],
        sek: typing.Callable[[], T_Result],
        chf: typing.Callable[[], T_Result],
        ars: typing.Callable[[], T_Result],
        brl: typing.Callable[[], T_Result],
        hkd: typing.Callable[[], T_Result],
        nok: typing.Callable[[], T_Result],
        php: typing.Callable[[], T_Result],
        pln: typing.Callable[[], T_Result],
        rub: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostMyFollowsSearchRequestCurrency.USD:
            return usd()
        if self is PostMyFollowsSearchRequestCurrency.CAD:
            return cad()
        if self is PostMyFollowsSearchRequestCurrency.EUR:
            return eur()
        if self is PostMyFollowsSearchRequestCurrency.GBP:
            return gbp()
        if self is PostMyFollowsSearchRequestCurrency.AUD:
            return aud()
        if self is PostMyFollowsSearchRequestCurrency.JPY:
            return jpy()
        if self is PostMyFollowsSearchRequestCurrency.NZD:
            return nzd()
        if self is PostMyFollowsSearchRequestCurrency.MXN:
            return mxn()
        if self is PostMyFollowsSearchRequestCurrency.DKK:
            return dkk()
        if self is PostMyFollowsSearchRequestCurrency.SEK:
            return sek()
        if self is PostMyFollowsSearchRequestCurrency.CHF:
            return chf()
        if self is PostMyFollowsSearchRequestCurrency.ARS:
            return ars()
        if self is PostMyFollowsSearchRequestCurrency.BRL:
            return brl()
        if self is PostMyFollowsSearchRequestCurrency.HKD:
            return hkd()
        if self is PostMyFollowsSearchRequestCurrency.NOK:
            return nok()
        if self is PostMyFollowsSearchRequestCurrency.PHP:
            return php()
        if self is PostMyFollowsSearchRequestCurrency.PLN:
            return pln()
        if self is PostMyFollowsSearchRequestCurrency.RUB:
            return rub()
