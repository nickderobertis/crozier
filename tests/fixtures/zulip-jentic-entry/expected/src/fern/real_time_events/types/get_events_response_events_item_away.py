

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_away_reaction_type import GetEventsResponseEventsItemAwayReactionType
from .get_events_response_events_item_away_type import GetEventsResponseEventsItemAwayType


class GetEventsResponseEventsItemAway(UniversalBaseModel):
    """
    Event sent to all users who can access the modified
    user when the status of a user changes.

    **Changes**: Prior to Zulip 8.0 (feature level 228),
    this event was sent to all users in the organization.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemAwayType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    away: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the user has marked themself "away" with this status.
    
    **Changes**: Deprecated in Zulip 6.0 (feature level 148);
    starting with that feature level, `away` is a legacy way to
    access the user's `presence_enabled` setting, with
    `away = !presence_enabled`. To be removed in a future release.
    """

    status_text: typing.Optional[str] = pydantic.Field(default=None)
    """
    The text content of the status message.
    
    This will be `""` for users who set a status without selecting
    or writing a message.
    """

    emoji_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The [emoji name](/api/update-status#parameter-emoji_name) for
    the emoji the user selected for their new status.
    
    This will be `""` for users who set a status without selecting
    an emoji.
    
    **Changes**: New in Zulip 5.0 (feature level 86).
    """

    emoji_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The [emoji code](/api/update-status#parameter-emoji_code) for
    the emoji the user selected for their new status.
    
    This will be `""` for users who set a status without selecting
    an emoji.
    
    **Changes**: New in Zulip 5.0 (feature level 86).
    """

    reaction_type: typing.Optional[GetEventsResponseEventsItemAwayReactionType] = pydantic.Field(default=None)
    """
    The [emoji type](/api/update-status#parameter-reaction_type) for
    the emoji the user selected for their new status.
    
    This will be `""` for users who set a status without selecting
    an emoji.
    
    **Changes**: New in Zulip 5.0 (feature level 86).
    """

    user_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the user whose status changed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
