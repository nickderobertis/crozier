

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pay import Pay


class DistributionBreakdown(UniversalBaseModel):
    """
    Information about the accounts that the payment was distributed to.
    """

    account_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the account for the given distribution.
    """

    bank_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the bank that the payment is being deposited to.
    """

    current_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    The amount distributed to this account.
    """

    current_pay: typing.Optional[Pay] = None
    iso_currency_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ISO-4217 currency code of the net pay. Always `null` if `unofficial_currency_code` is non-null.
    """

    mask: typing.Optional[str] = pydantic.Field(default=None)
    """
    The last 2-4 alphanumeric characters of an account's official account number.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Type of the account that the paystub was sent to (e.g. 'checking').
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
