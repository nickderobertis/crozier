

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .delivery_event import DeliveryEvent
from .message_summary_direction import MessageSummaryDirection
from .message_summary_object import MessageSummaryObject


class MessageSummary(UniversalBaseModel):
    object: MessageSummaryObject = pydantic.Field()
    """
    Object type identifier
    """

    created_at: dt.datetime = pydantic.Field()
    """
    When the message was created
    """

    updated_at: dt.datetime = pydantic.Field()
    """
    When the message was last updated
    """

    sent_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When the message was sent
    """

    delivered_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When the message was delivered
    """

    retain_until: dt.datetime = pydantic.Field()
    """
    When the message data will be purged
    """

    direction: MessageSummaryDirection = pydantic.Field()
    """
    Message direction
    """

    is_bounce_notification: bool = pydantic.Field()
    """
    Whether this is a bounce notification
    """

    bounce_classification: str = pydantic.Field()
    """
    Classification of bounce if applicable
    """

    delivery_attempts: typing.List[DeliveryEvent] = pydantic.Field()
    """
    List of delivery attempts for this message
    """

    message_id: str = pydantic.Field()
    """
    Message-ID header value
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    API-generated message ID
    """

    subject: str = pydantic.Field()
    """
    Message subject
    """

    tags: typing.List[str] = pydantic.Field()
    """
    Tags associated with the message
    """

    sender: str = pydantic.Field()
    """
    Sender email address
    """

    recipient: str = pydantic.Field()
    """
    Recipient email address
    """

    status: str = pydantic.Field()
    """
    Current message status
    """

    num_attempts: int = pydantic.Field()
    """
    Number of delivery attempts
    """

    click_count: int = pydantic.Field()
    """
    Number of clicks tracked for this message
    """

    open_count: int = pydantic.Field()
    """
    Number of opens tracked for this message
    """

    reference_message_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    ID of the original message (for bounce messages)
    """

    domain_id: str = pydantic.Field()
    """
    Domain ID this message was sent from
    """

    account_id: str = pydantic.Field()
    """
    Account ID this message belongs to
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
