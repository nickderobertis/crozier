

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .card_response import CardResponse
from .device import Device
from .elv_card_account import ElvCardAccount
from .event import Event
from .horizontal_accuracy import HorizontalAccuracy
from .lat import Lat
from .link import Link
from .lon import Lon
from .product import Product
from .transaction_base import TransactionBase
from .transaction_checkout_info import TransactionCheckoutInfo
from .transaction_event import TransactionEvent
from .transaction_full_location import TransactionFullLocation
from .transaction_full_payout_type import TransactionFullPayoutType
from .transaction_full_process_as import TransactionFullProcessAs
from .transaction_full_simple_payment_type import TransactionFullSimplePaymentType
from .transaction_full_simple_status import TransactionFullSimpleStatus
from .transaction_full_vat_rates_item import TransactionFullVatRatesItem
from .transaction_full_verification_method import TransactionFullVerificationMethod
from .transaction_mixin_history import TransactionMixinHistory


class TransactionFull(TransactionBase, TransactionCheckoutInfo, TransactionMixinHistory):
    """
    Full transaction resource with checkout, payout, and event details.
    """

    foreign_transaction_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    External transaction identifier supplied by the client.
    """

    client_transaction_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Client-supplied identifier of the transaction.
    """

    username: typing.Optional[str] = pydantic.Field(default=None)
    """
    Email address of the registered user (merchant) to whom the payment is made.
    """

    fee_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Transaction SumUp total fee amount.
    """

    lat: typing.Optional[Lat] = None
    lon: typing.Optional[Lon] = None
    horizontal_accuracy: typing.Optional[HorizontalAccuracy] = None
    merchant_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Internal SumUp identifier of the merchant.
    """

    device_info: typing.Optional[Device] = None
    simple_payment_type: typing.Optional[TransactionFullSimplePaymentType] = pydantic.Field(default=None)
    """
    Simple name of the payment type.
    """

    verification_method: typing.Optional[TransactionFullVerificationMethod] = pydantic.Field(default=None)
    """
    Verification method used for the transaction.
    """

    card: typing.Optional[CardResponse] = None
    elv_account: typing.Optional[ElvCardAccount] = None
    local_time: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Local timestamp of when the transaction was created.
    """

    payout_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The date of the payout.
    """

    payout_type: typing.Optional[TransactionFullPayoutType] = pydantic.Field(default=None)
    """
    Payout type for the transaction.
    """

    process_as: typing.Optional[TransactionFullProcessAs] = pydantic.Field(default=None)
    """
    Whether the transaction was processed as credit or debit.
    """

    products: typing.Optional[typing.List[Product]] = pydantic.Field(default=None)
    """
    List of products from the merchant's catalogue for which the transaction serves as a payment.
    """

    vat_rates: typing.Optional[typing.List[TransactionFullVatRatesItem]] = pydantic.Field(default=None)
    """
    List of VAT rates applicable to the transaction.
    """

    transaction_events: typing.Optional[typing.List[TransactionEvent]] = pydantic.Field(default=None)
    """
    Detailed list of events related to the transaction.
    """

    simple_status: typing.Optional[TransactionFullSimpleStatus] = pydantic.Field(default=None)
    """
    High-level status of the transaction from the merchant's perspective.
    
    - `PENDING`: The payment has been initiated and is still being processed. A final outcome is not available yet.
    - `SUCCESSFUL`: The payment was completed successfully.
    - `PAID_OUT`: The payment was completed successfully and the funds have already been included in a payout to the merchant.
    - `FAILED`: The payment did not complete successfully.
    - `CANCELLED`: The payment was cancelled or reversed and is no longer payable or payable to the merchant.
    - `CANCEL_FAILED`: An attempt to cancel or reverse the payment was not completed successfully.
    - `REFUNDED`: The payment was refunded in full or in part.
    - `REFUND_FAILED`: An attempt to refund the payment was not completed successfully.
    - `CHARGEBACK`: The payment was subject to a chargeback.
    - `NON_COLLECTION`: The amount could not be collected from the merchant after a chargeback or related adjustment.
    """

    links: typing.Optional[typing.List[Link]] = pydantic.Field(default=None)
    """
    List of hyperlinks for accessing related resources.
    """

    events: typing.Optional[typing.List[Event]] = pydantic.Field(default=None)
    """
    Compact list of events related to the transaction.
    """

    location: typing.Optional[TransactionFullLocation] = pydantic.Field(default=None)
    """
    Details of the payment location as received from the payment terminal.
    """

    tax_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether tax deduction is enabled for the transaction.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
