

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Currency(enum.StrEnum):
    """
    Three-letter [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code of the amount.
    """

    BGN = "BGN"
    BRL = "BRL"
    CHF = "CHF"
    CLP = "CLP"
    COP = "COP"
    CZK = "CZK"
    DKK = "DKK"
    EUR = "EUR"
    GBP = "GBP"
    HRK = "HRK"
    HUF = "HUF"
    NOK = "NOK"
    PLN = "PLN"
    RON = "RON"
    SEK = "SEK"
    USD = "USD"

    def visit(
        self,
        bgn: typing.Callable[[], T_Result],
        brl: typing.Callable[[], T_Result],
        chf: typing.Callable[[], T_Result],
        clp: typing.Callable[[], T_Result],
        cop: typing.Callable[[], T_Result],
        czk: typing.Callable[[], T_Result],
        dkk: typing.Callable[[], T_Result],
        eur: typing.Callable[[], T_Result],
        gbp: typing.Callable[[], T_Result],
        hrk: typing.Callable[[], T_Result],
        huf: typing.Callable[[], T_Result],
        nok: typing.Callable[[], T_Result],
        pln: typing.Callable[[], T_Result],
        ron: typing.Callable[[], T_Result],
        sek: typing.Callable[[], T_Result],
        usd: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Currency.BGN:
            return bgn()
        if self is Currency.BRL:
            return brl()
        if self is Currency.CHF:
            return chf()
        if self is Currency.CLP:
            return clp()
        if self is Currency.COP:
            return cop()
        if self is Currency.CZK:
            return czk()
        if self is Currency.DKK:
            return dkk()
        if self is Currency.EUR:
            return eur()
        if self is Currency.GBP:
            return gbp()
        if self is Currency.HRK:
            return hrk()
        if self is Currency.HUF:
            return huf()
        if self is Currency.NOK:
            return nok()
        if self is Currency.PLN:
            return pln()
        if self is Currency.RON:
            return ron()
        if self is Currency.SEK:
            return sek()
        if self is Currency.USD:
            return usd()
