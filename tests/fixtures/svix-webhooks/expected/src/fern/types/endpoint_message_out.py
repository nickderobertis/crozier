

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .message_status import MessageStatus
from .message_status_text import MessageStatusText


class EndpointMessageOut(UniversalBaseModel):
    """
    A model containing information on a given message plus additional fields on the last attempt for that message.
    """

    channels: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of free-form identifiers that endpoints can filter by
    """

    event_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="eventId"),
        pydantic.Field(alias="eventId", description="Optional unique identifier for the message"),
    ] = None
    """
    Optional unique identifier for the message
    """

    event_type: typing_extensions.Annotated[str, FieldMetadata(alias="eventType"), pydantic.Field(alias="eventType")]
    id: str
    next_attempt: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="nextAttempt"), pydantic.Field(alias="nextAttempt")
    ] = None
    payload: typing.Dict[str, typing.Any]
    status: MessageStatus
    status_text: typing_extensions.Annotated[
        MessageStatusText, FieldMetadata(alias="statusText"), pydantic.Field(alias="statusText")
    ]
    timestamp: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
