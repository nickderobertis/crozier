

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_muted_users_muted_users_item import (
    GetEventsResponseEventsItemMutedUsersMutedUsersItem,
)
from .get_events_response_events_item_muted_users_type import GetEventsResponseEventsItemMutedUsersType


class GetEventsResponseEventsItemMutedUsers(UniversalBaseModel):
    """
    Event sent to a user's clients when that user's set of
    configured [muted users](/api/mute-user) have changed.

    **Changes**: New in Zulip 4.0 (feature level 48).
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemMutedUsersType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    muted_users: typing.Optional[typing.List[GetEventsResponseEventsItemMutedUsersMutedUsersItem]] = pydantic.Field(
        default=None
    )
    """
    A list of dictionaries where each dictionary describes
    a muted user.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
