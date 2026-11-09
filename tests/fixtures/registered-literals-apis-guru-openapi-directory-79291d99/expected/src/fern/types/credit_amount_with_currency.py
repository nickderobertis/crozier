

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credit_iso_currency_code import CreditIsoCurrencyCode
from .credit_unofficial_currency_code import CreditUnofficialCurrencyCode


class CreditAmountWithCurrency(UniversalBaseModel):
    """
    This contains an amount, denominated in the currency specified by either `iso_currency_code` or `unofficial_currency_code`
    """

    amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Value of amount with up to 2 decimal places.
    """

    iso_currency_code: typing.Optional[CreditIsoCurrencyCode] = None
    unofficial_currency_code: typing.Optional[CreditUnofficialCurrencyCode] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
