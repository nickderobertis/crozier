

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .receipt_card import ReceiptCard
from .receipt_event import ReceiptEvent
from .receipt_reader import ReceiptReader
from .receipt_transaction_process_as import ReceiptTransactionProcessAs
from .receipt_transaction_products_item import ReceiptTransactionProductsItem
from .receipt_transaction_vat_rates_item import ReceiptTransactionVatRatesItem
from .transaction_id import TransactionId


class ReceiptTransaction(UniversalBaseModel):
    """
    Transaction details displayed on a receipt.
    """

    transaction_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Transaction code returned after processing the transaction.
    """

    transaction_id: typing.Optional[TransactionId] = None
    merchant_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Short unique identifier for the merchant.
    """

    amount: typing.Optional[str] = pydantic.Field(default=None)
    """
    Total transaction amount, in major units.
    """

    vat_amount: typing.Optional[str] = pydantic.Field(default=None)
    """
    VAT included in the transaction amount, in major units.
    """

    tip_amount: typing.Optional[str] = pydantic.Field(default=None)
    """
    Tip included in the transaction amount, in major units.
    """

    currency: typing.Optional[str] = pydantic.Field(default=None)
    """
    Three-letter ISO 4217 currency code of the transaction.
    """

    timestamp: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The timestamp of when the transaction was created.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Current processing status of the transaction.
    """

    payment_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Payment type used for the transaction.
    """

    entry_mode: typing.Optional[str] = pydantic.Field(default=None)
    """
    Entry mode of the payment details.
    """

    verification_method: typing.Optional[str] = pydantic.Field(default=None)
    """
    Cardholder verification method.
    """

    card_reader: typing.Optional[ReceiptReader] = None
    card: typing.Optional[ReceiptCard] = None
    installments_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of installments.
    """

    process_as: typing.Optional[ReceiptTransactionProcessAs] = pydantic.Field(default=None)
    """
    Whether the transaction was processed as credit or debit.
    """

    products: typing.Optional[typing.List[ReceiptTransactionProductsItem]] = pydantic.Field(default=None)
    """
    Products associated with the transaction.
    """

    vat_rates: typing.Optional[typing.List[ReceiptTransactionVatRatesItem]] = pydantic.Field(default=None)
    """
    VAT breakdown for the transaction.
    """

    events: typing.Optional[typing.List[ReceiptEvent]] = pydantic.Field(default=None)
    """
    Transaction events displayed on the receipt.
    """

    receipt_no: typing.Optional[str] = pydantic.Field(default=None)
    """
    Receipt number associated with the transaction.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
