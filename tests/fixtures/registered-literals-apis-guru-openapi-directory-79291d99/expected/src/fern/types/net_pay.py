

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .total import Total


class NetPay(UniversalBaseModel):
    """
    An object representing information about the net pay amount on the paystub.
    """

    current_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Raw amount of the net pay for the pay period
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the net pay
    """

    iso_currency_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ISO-4217 currency code of the net pay. Always `null` if `unofficial_currency_code` is non-null.
    """

    total: typing.Optional[Total] = None
    unofficial_currency_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unofficial currency code associated with the net pay. Always `null` if `iso_currency_code` is non-`null`. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.
    
    See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s.
    """

    ytd_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    The year-to-date amount of the net pay
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
