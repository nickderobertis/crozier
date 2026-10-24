

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetricObservationCurrency(enum.StrEnum):
    """
    Required for unit=currency and null for non-monetary observations. Missing monetary currency is quarantined instead of inferred.
    """

    AED = "AED"
    AUD = "AUD"
    BRL = "BRL"
    CAD = "CAD"
    EGP = "EGP"
    EUR = "EUR"
    GBP = "GBP"
    INR = "INR"
    JPY = "JPY"
    MXN = "MXN"
    PLN = "PLN"
    SAR = "SAR"
    SEK = "SEK"
    SGD = "SGD"
    TRY = "TRY"
    USD = "USD"

    def visit(
        self,
        aed: typing.Callable[[], T_Result],
        aud: typing.Callable[[], T_Result],
        brl: typing.Callable[[], T_Result],
        cad: typing.Callable[[], T_Result],
        egp: typing.Callable[[], T_Result],
        eur: typing.Callable[[], T_Result],
        gbp: typing.Callable[[], T_Result],
        inr: typing.Callable[[], T_Result],
        jpy: typing.Callable[[], T_Result],
        mxn: typing.Callable[[], T_Result],
        pln: typing.Callable[[], T_Result],
        sar: typing.Callable[[], T_Result],
        sek: typing.Callable[[], T_Result],
        sgd: typing.Callable[[], T_Result],
        try_: typing.Callable[[], T_Result],
        usd: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MetricObservationCurrency.AED:
            return aed()
        if self is MetricObservationCurrency.AUD:
            return aud()
        if self is MetricObservationCurrency.BRL:
            return brl()
        if self is MetricObservationCurrency.CAD:
            return cad()
        if self is MetricObservationCurrency.EGP:
            return egp()
        if self is MetricObservationCurrency.EUR:
            return eur()
        if self is MetricObservationCurrency.GBP:
            return gbp()
        if self is MetricObservationCurrency.INR:
            return inr()
        if self is MetricObservationCurrency.JPY:
            return jpy()
        if self is MetricObservationCurrency.MXN:
            return mxn()
        if self is MetricObservationCurrency.PLN:
            return pln()
        if self is MetricObservationCurrency.SAR:
            return sar()
        if self is MetricObservationCurrency.SEK:
            return sek()
        if self is MetricObservationCurrency.SGD:
            return sgd()
        if self is MetricObservationCurrency.TRY:
            return try_()
        if self is MetricObservationCurrency.USD:
            return usd()
