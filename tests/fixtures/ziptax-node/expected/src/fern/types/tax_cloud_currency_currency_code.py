

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TaxCloudCurrencyCurrencyCode(enum.StrEnum):
    """
    ISO 4217 currency code the line-item prices are denominated in. USD or CAD. Defaults to USD when omitted.
    """

    USD = "USD"
    CAD = "CAD"

    def visit(self, usd: typing.Callable[[], T_Result], cad: typing.Callable[[], T_Result]) -> T_Result:
        if self is TaxCloudCurrencyCurrencyCode.USD:
            return usd()
        if self is TaxCloudCurrencyCurrencyCode.CAD:
            return cad()
