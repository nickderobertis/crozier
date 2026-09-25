

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_msg_type_type import GetEventsResponseEventsItemMsgTypeType


class GetEventsResponseEventsItemMsgType(UniversalBaseModel):
    """
    Event sent when a submessage is added to a message.

    Submessages are an **experimental** API used for widgets such as the
    `/poll` widget in Zulip.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemMsgTypeType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    msg_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of the message.
    """

    content: typing.Optional[str] = pydantic.Field(default=None)
    """
    The new content of the submessage.
    """

    message_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the message to which the submessage has been added.
    """

    sender_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the user who sent the message.
    """

    submessage_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the submessage.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
