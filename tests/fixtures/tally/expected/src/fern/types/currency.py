

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Currency(enum.StrEnum):
    USD = "USD"
    EUR = "EUR"
    GBP = "GBP"
    CAD = "CAD"
    AUD = "AUD"
    JPY = "JPY"
    CNY = "CNY"
    INR = "INR"

    def visit(
        self,
        usd: typing.Callable[[], T_Result],
        eur: typing.Callable[[], T_Result],
        gbp: typing.Callable[[], T_Result],
        cad: typing.Callable[[], T_Result],
        aud: typing.Callable[[], T_Result],
        jpy: typing.Callable[[], T_Result],
        cny: typing.Callable[[], T_Result],
        inr: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Currency.USD:
            return usd()
        if self is Currency.EUR:
            return eur()
        if self is Currency.GBP:
            return gbp()
        if self is Currency.CAD:
            return cad()
        if self is Currency.AUD:
            return aud()
        if self is Currency.JPY:
            return jpy()
        if self is Currency.CNY:
            return cny()
        if self is Currency.INR:
            return inr()
