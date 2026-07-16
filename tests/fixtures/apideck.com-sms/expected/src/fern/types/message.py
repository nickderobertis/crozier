

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .message_direction import MessageDirection
from .message_error import MessageError
from .message_price import MessagePrice
from .message_status import MessageStatus
from .message_type import MessageType


class Message(UniversalBaseModel):
    body: str = pydantic.Field()
    """
    The message text.
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time when the object was created.
    """

    created_by: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user who created the object.
    """

    direction: typing.Optional[MessageDirection] = pydantic.Field(default=None)
    """
    The direction of the message.
    """

    error: typing.Optional[MessageError] = pydantic.Field(default=None)
    """
    The error returned if your message status is failed or undelivered.
    """

    from_: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="from"),
        pydantic.Field(alias="from", description="The phone number that initiated the message."),
    ]
    """
    The phone number that initiated the message.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique identifier for an object.
    """

    messaging_service_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the Messaging Service used with the message. In case of Plivo this links to the Powerpack ID.
    """

    number_of_media_files: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of media files associated with the message.
    """

    number_of_units: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of units that make up the complete message. Messages can be split up due to the constraints of the message size.
    """

    price: typing.Optional[MessagePrice] = pydantic.Field(default=None)
    """
    Price of the message.
    """

    reference: typing.Optional[str] = pydantic.Field(default=None)
    """
    A client reference.
    """

    scheduled_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The scheduled date and time of the message.
    """

    sent_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time that the message was sent
    """

    status: typing.Optional[MessageStatus] = pydantic.Field(default=None)
    """
    Status of the delivery of the message.
    """

    subject: typing.Optional[str] = None
    to: str = pydantic.Field()
    """
    The phone number that received the message.
    """

    type: typing.Optional[MessageType] = pydantic.Field(default=None)
    """
    Set to sms for SMS messages and mms for MMS messages.
    """

    updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time when the object was last updated.
    """

    updated_by: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user who last updated the object.
    """

    webhook_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Define a webhook to receive delivery notifications.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
