

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetV1MetricObservationsRequestCurrency(enum.StrEnum):
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
        if self is GetV1MetricObservationsRequestCurrency.AED:
            return aed()
        if self is GetV1MetricObservationsRequestCurrency.AUD:
            return aud()
        if self is GetV1MetricObservationsRequestCurrency.BRL:
            return brl()
        if self is GetV1MetricObservationsRequestCurrency.CAD:
            return cad()
        if self is GetV1MetricObservationsRequestCurrency.EGP:
            return egp()
        if self is GetV1MetricObservationsRequestCurrency.EUR:
            return eur()
        if self is GetV1MetricObservationsRequestCurrency.GBP:
            return gbp()
        if self is GetV1MetricObservationsRequestCurrency.INR:
            return inr()
        if self is GetV1MetricObservationsRequestCurrency.JPY:
            return jpy()
        if self is GetV1MetricObservationsRequestCurrency.MXN:
            return mxn()
        if self is GetV1MetricObservationsRequestCurrency.PLN:
            return pln()
        if self is GetV1MetricObservationsRequestCurrency.SAR:
            return sar()
        if self is GetV1MetricObservationsRequestCurrency.SEK:
            return sek()
        if self is GetV1MetricObservationsRequestCurrency.SGD:
            return sgd()
        if self is GetV1MetricObservationsRequestCurrency.TRY:
            return try_()
        if self is GetV1MetricObservationsRequestCurrency.USD:
            return usd()
