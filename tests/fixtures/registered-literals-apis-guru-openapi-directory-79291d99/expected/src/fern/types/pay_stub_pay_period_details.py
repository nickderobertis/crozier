

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credit_pay_stub_pay_basis_type import CreditPayStubPayBasisType
from .pay_stub_distribution_breakdown import PayStubDistributionBreakdown


class PayStubPayPeriodDetails(UniversalBaseModel):
    """
    Details about the pay period.
    """

    distribution_breakdown: typing.List[PayStubDistributionBreakdown]
    end_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The date on which the pay period ended, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ("yyyy-mm-dd").
    """

    gross_earnings: typing.Optional[float] = pydantic.Field(default=None)
    """
    Total earnings before tax/deductions.
    """

    iso_currency_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ISO-4217 currency code of the net pay. Always `null` if `unofficial_currency_code` is non-null.
    """

    pay_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    The amount of the paycheck.
    """

    pay_basis: typing.Optional[CreditPayStubPayBasisType] = None
    pay_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The date on which the pay stub was issued, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ("yyyy-mm-dd").
    """

    pay_frequency: typing.Optional[str] = pydantic.Field(default=None)
    """
    The frequency at which an individual is paid.
    """

    start_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The date on which the pay period started, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ("yyyy-mm-dd").
    """

    unofficial_currency_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unofficial currency code associated with the net pay. Always `null` if `iso_currency_code` is non-`null`. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.
    
    See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
