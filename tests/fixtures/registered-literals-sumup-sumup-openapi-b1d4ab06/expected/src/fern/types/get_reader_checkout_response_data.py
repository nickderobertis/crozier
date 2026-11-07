

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_reader_checkout_response_data_card_type import GetReaderCheckoutResponseDataCardType
from .get_reader_checkout_response_data_payment_type import GetReaderCheckoutResponseDataPaymentType
from .get_reader_checkout_response_data_status import GetReaderCheckoutResponseDataStatus
from .get_reader_checkout_response_data_total_amount import GetReaderCheckoutResponseDataTotalAmount


class GetReaderCheckoutResponseData(UniversalBaseModel):
    card_type: typing.Optional[GetReaderCheckoutResponseDataCardType] = pydantic.Field(default=None)
    """
    Type of the card. Required for some countries
    """

    checkout_id: str = pydantic.Field()
    """
    Unique identifier for the checkout
    """

    client_transaction_id: str = pydantic.Field()
    """
    Client transaction identifier associated with the checkout
    """

    created_at: dt.datetime = pydantic.Field()
    """
    Checkout creation timestamp
    """

    installments: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of installments for the transaction. Required for some countries.
    """

    payment_failure_reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    Payment failure reason
    """

    payment_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Payment status from payments v2 event
    """

    payment_type: GetReaderCheckoutResponseDataPaymentType = pydantic.Field()
    """
    Type of the payment. Required for some countries
    """

    reader_firmware_version: str = pydantic.Field()
    """
    Reader firmware version
    """

    reader_serial_number: str = pydantic.Field()
    """
    Device serial number
    """

    status: GetReaderCheckoutResponseDataStatus = pydantic.Field()
    """
    Current status of the checkout
    """

    total_amount: GetReaderCheckoutResponseDataTotalAmount = pydantic.Field()
    """
    Amount structure.
    
    The amount is represented as an integer value altogether with the currency and the minor unit.
    
    For example, EUR 1.00 is represented as value 100 with minor unit of 2.
    """

    updated_at: dt.datetime = pydantic.Field()
    """
    Checkout last update timestamp
    """

    valid_until: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Checkout expiration timestamp. After this time, the checkout will be automatically cancelled.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
