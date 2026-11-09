

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credit_iso_currency_code import CreditIsoCurrencyCode
from .credit_unofficial_currency_code import CreditUnofficialCurrencyCode


class CreditBankIncomeTransaction(UniversalBaseModel):
    """
    The transactions data for the end user's income source(s).
    """

    amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    The settled value of the transaction, denominated in the transactions's currency as stated in `iso_currency_code` or `unofficial_currency_code`.
    Positive values when money moves out of the account; negative values when money moves in.
    For example, credit card purchases are positive; credit card payment, direct deposits, and refunds are negative.
    """

    check_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The check number of the transaction. This field is only populated for check transactions.
    """

    date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    For pending transactions, the date that the transaction occurred; for posted transactions, the date that the transaction posted.
    Both dates are returned in an ISO 8601 format (YYYY-MM-DD).
    """

    iso_currency_code: typing.Optional[CreditIsoCurrencyCode] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The merchant name or transaction description.
    """

    original_description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The string returned by the financial institution to describe the transaction.
    """

    pending: typing.Optional[bool] = pydantic.Field(default=None)
    """
    When true, identifies the transaction as pending or unsettled.
    Pending transaction details (name, type, amount, category ID) may change before they are settled.
    """

    transaction_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique ID of the transaction. Like all Plaid identifiers, the `transaction_id` is case sensitive.
    """

    unofficial_currency_code: typing.Optional[CreditUnofficialCurrencyCode] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
