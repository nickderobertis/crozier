

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_events_response_events_item_email_presence_value_status import (
    GetEventsResponseEventsItemEmailPresenceValueStatus,
)


class GetEventsResponseEventsItemEmailPresenceValue(UniversalBaseModel):
    """
    `{client_name}`: Object containing the details of the user's
    presence.

    **Changes**: Starting with Zulip 7.0 (feature level 178), this
    will always be `"website"` as the server no longer stores which
    client submitted presence updates.

    Previously, the object key was the client's platform name, for
    example `website` or `ZulipDesktop`.
    """

    client: typing.Optional[str] = pydantic.Field(default=None)
    """
    The client's platform name.
    
    **Changes**: Starting with Zulip 7.0 (feature level 178), this
    will always be `"website"` as the server no longer stores which
    client submitted presence updates.
    """

    status: typing.Optional[GetEventsResponseEventsItemEmailPresenceValueStatus] = pydantic.Field(default=None)
    """
    The status of the user on this client. Will be either `idle`
    or `active`.
    """

    timestamp: typing.Optional[int] = pydantic.Field(default=None)
    """
    The UNIX timestamp of when this client sent the user's presence
    to the server with the precision of a second.
    """

    pushable: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the client is capable of showing mobile/push notifications
    to the user.
    
    **Changes**: Starting with Zulip 7.0 (feature level 178), this
    will always be `false` as the server no longer stores which
    client submitted presence updates.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
