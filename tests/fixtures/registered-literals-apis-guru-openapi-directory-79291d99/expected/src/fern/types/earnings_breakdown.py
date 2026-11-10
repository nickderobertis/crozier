

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .earnings_breakdown_canonical_description import EarningsBreakdownCanonicalDescription


class EarningsBreakdown(UniversalBaseModel):
    """
    An object representing the earnings line items for the pay period.
    """

    canonical_description: typing.Optional[EarningsBreakdownCanonicalDescription] = None
    current_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Raw amount of the earning line item.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the earning line item.
    """

    hours: typing.Optional[float] = pydantic.Field(default=None)
    """
    Number of hours applicable for this earning.
    """

    iso_currency_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ISO-4217 currency code of the line item. Always `null` if `unofficial_currency_code` is non-null.
    """

    rate: typing.Optional[float] = pydantic.Field(default=None)
    """
    Hourly rate applicable for this earning.
    """

    unofficial_currency_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unofficial currency code associated with the line item. Always `null` if `iso_currency_code` is non-`null`. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.
    
    See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s.
    """

    ytd_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    The year-to-date amount of the deduction.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
