

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PutListingsSlugRequestShippingRatesItemRateCurrency(str, enum.Enum):
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
        if self is PutListingsSlugRequestShippingRatesItemRateCurrency.USD:
            return usd()
        if self is PutListingsSlugRequestShippingRatesItemRateCurrency.CAD:
            return cad()
        if self is PutListingsSlugRequestShippingRatesItemRateCurrency.EUR:
            return eur()
        if self is PutListingsSlugRequestShippingRatesItemRateCurrency.GBP:
            return gbp()
        if self is PutListingsSlugRequestShippingRatesItemRateCurrency.AUD:
            return aud()
        if self is PutListingsSlugRequestShippingRatesItemRateCurrency.JPY:
            return jpy()
        if self is PutListingsSlugRequestShippingRatesItemRateCurrency.NZD:
            return nzd()
        if self is PutListingsSlugRequestShippingRatesItemRateCurrency.MXN:
            return mxn()
