

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DeductionsBreakdown(UniversalBaseModel):
    """
    An object representing the deduction line items for the pay period
    """

    current_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Raw amount of the deduction
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the deduction line item
    """

    iso_currency_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ISO-4217 currency code of the line item. Always `null` if `unofficial_currency_code` is non-null.
    """

    unofficial_currency_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unofficial currency code associated with the line item. Always `null` if `iso_currency_code` is non-`null`. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.
    
    See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s.
    """

    ytd_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    The year-to-date amount of the deduction
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
