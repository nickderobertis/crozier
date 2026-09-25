

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_channel_folder_id_data import GetEventsResponseEventsItemChannelFolderIdData
from .get_events_response_events_item_channel_folder_id_op import GetEventsResponseEventsItemChannelFolderIdOp
from .get_events_response_events_item_channel_folder_id_type import GetEventsResponseEventsItemChannelFolderIdType


class GetEventsResponseEventsItemChannelFolderId(UniversalBaseModel):
    """
    Event sent to users in an organization when a channel folder is updated.

    **Changes**: New in Zulip 11.0 (feature level 389).
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemChannelFolderIdType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemChannelFolderIdOp] = None
    channel_folder_id: typing.Optional[float] = pydantic.Field(default=None)
    """
    ID of the updated channel folder.
    """

    data: typing.Optional[GetEventsResponseEventsItemChannelFolderIdData] = pydantic.Field(default=None)
    """
    Dictionary containing the changed details of the channel folder.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
