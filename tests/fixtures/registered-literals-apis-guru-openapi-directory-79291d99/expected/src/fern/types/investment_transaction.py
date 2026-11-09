

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .investment_transaction_subtype import InvestmentTransactionSubtype
from .investment_transaction_type import InvestmentTransactionType


class InvestmentTransaction(UniversalBaseModel):
    """
    A transaction within an investment account.
    """

    account_id: str = pydantic.Field()
    """
    The `account_id` of the account against which this transaction posted.
    """

    amount: float = pydantic.Field()
    """
    The complete value of the transaction. Positive values when cash is debited, e.g. purchases of stock; negative values when cash is credited, e.g. sales of stock. Treatment remains the same for cash-only movements unassociated with securities.
    """

    cancel_transaction_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A legacy field formerly used internally by Plaid to identify certain canceled transactions.
    """

    date: dt.date = pydantic.Field()
    """
    The [ISO 8601](https://wikipedia.org/wiki/ISO_8601) posting date for the transaction.
    """

    fees: typing.Optional[float] = pydantic.Field(default=None)
    """
    The combined value of all fees applied to this transaction
    """

    investment_transaction_id: str = pydantic.Field()
    """
    The ID of the Investment transaction, unique across all Plaid transactions. Like all Plaid identifiers, the `investment_transaction_id` is case sensitive.
    """

    iso_currency_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ISO-4217 currency code of the transaction. Always `null` if `unofficial_currency_code` is non-`null`.
    """

    name: str = pydantic.Field()
    """
    The institution’s description of the transaction.
    """

    price: float = pydantic.Field()
    """
    The price of the security at which this transaction occurred.
    """

    quantity: float = pydantic.Field()
    """
    The number of units of the security involved in this transaction. Positive for buy transactions; negative for sell transactions.
    """

    security_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The `security_id` to which this transaction is related.
    """

    subtype: InvestmentTransactionSubtype
    type: InvestmentTransactionType
    unofficial_currency_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unofficial currency code associated with the holding. Always `null` if `iso_currency_code` is non-`null`. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.
    
    See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
