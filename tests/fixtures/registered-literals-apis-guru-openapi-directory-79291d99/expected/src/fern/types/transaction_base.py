

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .location import Location
from .payment_meta import PaymentMeta
from .transaction_base_transaction_type import TransactionBaseTransactionType


class TransactionBase(UniversalBaseModel):
    """
    A representation of a transaction
    """

    account_id: str = pydantic.Field()
    """
    The ID of the account in which this transaction occurred.
    """

    account_owner: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the account owner. This field is not typically populated and only relevant when dealing with sub-accounts.
    """

    amount: float = pydantic.Field()
    """
    The settled value of the transaction, denominated in the transactions's currency, as stated in `iso_currency_code` or `unofficial_currency_code`. Positive values when money moves out of the account; negative values when money moves in. For example, debit card purchases are positive; credit card payments, direct deposits, and refunds are negative.
    """

    category: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A hierarchical array of the categories to which this transaction belongs. For a full list of categories, see [`/categories/get`](https://plaid.com/docs/api/products/transactions/#categoriesget).
    
    If the `transactions` object was returned by an Assets endpoint such as `/asset_report/get/` or `/asset_report/pdf/get`, this field will only appear in an Asset Report with Insights.
    """

    category_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the category to which this transaction belongs. For a full list of categories, see [`/categories/get`](https://plaid.com/docs/api/products/transactions/#categoriesget).
    
    If the `transactions` object was returned by an Assets endpoint such as `/asset_report/get/` or `/asset_report/pdf/get`, this field will only appear in an Asset Report with Insights.
    """

    check_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The check number of the transaction. This field is only populated for check transactions.
    """

    date: dt.date = pydantic.Field()
    """
    For pending transactions, the date that the transaction occurred; for posted transactions, the date that the transaction posted. Both dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ( `YYYY-MM-DD` ).
    """

    iso_currency_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ISO-4217 currency code of the transaction. Always `null` if `unofficial_currency_code` is non-null.
    """

    location: typing.Optional[Location] = None
    logo_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The logo associated with the merchant, if available. Formatted as a 100x100 pixels PNG file path.
    """

    merchant_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The merchant name, as enriched by Plaid from the `name` field. This is typically a more human-readable version of the merchant counterparty in the transaction. For some bank transactions (such as checks or account transfers) where there is no meaningful merchant name, this value will be `null`.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The merchant name or transaction description.
    
    If the `transactions` object was returned by a Transactions endpoint such as `/transactions/get`, this field will always appear. If the `transactions` object was returned by an Assets endpoint such as `/asset_report/get/` or `/asset_report/pdf/get`, this field will only appear in an Asset Report with Insights.
    """

    original_description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The string returned by the financial institution to describe the transaction. For transactions returned by `/transactions/get`, this field is in beta and will be omitted unless the client is both enrolled in the closed beta program and has set `options.include_original_description` to `true`.
    """

    payment_meta: typing.Optional[PaymentMeta] = None
    pending: bool = pydantic.Field()
    """
    When `true`, identifies the transaction as pending or unsettled. Pending transaction details (name, type, amount, category ID) may change before they are settled.
    """

    pending_transaction_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of a posted transaction's associated pending transaction, where applicable.
    """

    transaction_id: str = pydantic.Field()
    """
    The unique ID of the transaction. Like all Plaid identifiers, the `transaction_id` is case sensitive.
    """

    transaction_type: typing.Optional[TransactionBaseTransactionType] = pydantic.Field(default=None)
    """
    Please use the `payment_channel` field, `transaction_type` will be deprecated in the future.
    
    `digital:` transactions that took place online.
    
    `place:` transactions that were made at a physical location.
    
    `special:` transactions that relate to banks, e.g. fees or deposits.
    
    `unresolved:` transactions that do not fit into the other three types.
    """

    unofficial_currency_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unofficial currency code associated with the transaction. Always `null` if `iso_currency_code` is non-`null`. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.
    
    See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s.
    """

    website: typing.Optional[str] = pydantic.Field(default=None)
    """
    The website associated with the merchant, if available.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
