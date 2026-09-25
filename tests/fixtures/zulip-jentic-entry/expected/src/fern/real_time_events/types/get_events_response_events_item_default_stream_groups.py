

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.default_channel_group import DefaultChannelGroup
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_default_stream_groups_type import (
    GetEventsResponseEventsItemDefaultStreamGroupsType,
)


class GetEventsResponseEventsItemDefaultStreamGroups(UniversalBaseModel):
    """
    Event sent to all users in a Zulip organization when an organization
    administrator changes the organization's configured default channel groups.

    Default channel groups are an **experimental** feature that is not yet
    stabilized.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemDefaultStreamGroupsType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    default_stream_groups: typing.Optional[typing.List[DefaultChannelGroup]] = pydantic.Field(default=None)
    """
    An array of dictionaries where each dictionary
    contains details about a single default channel group.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
