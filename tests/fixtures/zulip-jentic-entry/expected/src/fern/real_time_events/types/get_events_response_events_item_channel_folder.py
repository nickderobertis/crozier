

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.channel_folder import ChannelFolder
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_channel_folder_op import GetEventsResponseEventsItemChannelFolderOp
from .get_events_response_events_item_channel_folder_type import GetEventsResponseEventsItemChannelFolderType


class GetEventsResponseEventsItemChannelFolder(UniversalBaseModel):
    """
    Event sent to users in an organization when a channel folder is created.

    **Changes**: New in Zulip 11.0 (feature level 389).
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemChannelFolderType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemChannelFolderOp] = None
    channel_folder: typing.Optional[ChannelFolder] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
