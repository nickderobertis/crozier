

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .payment_initiation_payment_status import PaymentInitiationPaymentStatus
from .plaid_error import PlaidError
from .webhook_environment_values import WebhookEnvironmentValues


class PaymentStatusUpdateWebhook(UniversalBaseModel):
    """
    Fired when the status of a payment has changed.
    """

    adjusted_reference: typing.Optional[str] = pydantic.Field(default=None)
    """
    The value of the reference sent to the bank after adjustment to pass bank validation rules.
    """

    adjusted_start_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The start date sent to the bank after adjusting for holidays or weekends.  Will be provided in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). If the start date did not require adjustment, or if the payment is not a standing order, this field will be `null`.
    """

    environment: WebhookEnvironmentValues
    error: typing.Optional[PlaidError] = None
    new_payment_status: PaymentInitiationPaymentStatus
    old_payment_status: PaymentInitiationPaymentStatus
    original_reference: typing.Optional[str] = pydantic.Field(default=None)
    """
    The original value of the reference when creating the payment.
    """

    original_start_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The original value of the `start_date` provided during the creation of a standing order. If the payment is not a standing order, this field will be `null`.
    """

    payment_id: str = pydantic.Field()
    """
    The `payment_id` for the payment being updated
    """

    timestamp: dt.datetime = pydantic.Field()
    """
    The timestamp of the update, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format, e.g. `"2017-09-14T14:42:19.350Z"`
    """

    transaction_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The transaction ID that this payment is associated with, if any. This is present only when a payment was initiated using virtual accounts.
    """

    webhook_code: str = pydantic.Field()
    """
    `PAYMENT_STATUS_UPDATE`
    """

    webhook_type: str = pydantic.Field()
    """
    `PAYMENT_INITIATION`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
