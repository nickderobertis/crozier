

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PayStubEarningsTotal(UniversalBaseModel):
    """
    An object representing both the current pay period and year to date amount for an earning category.
    """

    current_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Total amount of the earnings for this pay period.
    """

    hours: typing.Optional[float] = pydantic.Field(default=None)
    """
    Total number of hours worked for this pay period.
    """

    iso_currency_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ISO-4217 currency code of the line item. Always `null` if `unofficial_currency_code` is non-null.
    """

    unofficial_currency_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unofficial currency code associated with the security. Always `null` if `iso_currency_code` is non-`null`. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.
    
    See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s.
    """

    ytd_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    The total year-to-date amount of the earnings.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
