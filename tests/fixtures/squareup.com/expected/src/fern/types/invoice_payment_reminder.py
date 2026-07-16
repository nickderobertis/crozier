

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InvoicePaymentReminder(UniversalBaseModel):
    """
    Describes a payment request reminder (automatic notification) that Square sends
    to the customer. You configure a reminder relative to the payment request
    `due_date`.
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    The reminder message.
    """

    relative_scheduled_days: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of days before (a negative number) or after (a positive number)
    the payment request `due_date` when the reminder is sent. For example, -3 indicates that
    the reminder should be sent 3 days before the payment request `due_date`.
    """

    sent_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    If sent, the timestamp when the reminder was sent, in RFC 3339 format.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the reminder.
    """

    uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    A Square-assigned ID that uniquely identifies the reminder within the
    `InvoicePaymentRequest`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
