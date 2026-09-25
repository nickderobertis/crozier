

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_user_presence_response_presence_aggregated import GetUserPresenceResponsePresenceAggregated
from .get_user_presence_response_presence_website import GetUserPresenceResponsePresenceWebsite


class GetUserPresenceResponsePresence(UniversalBaseModel):
    """
    An object containing the presence details for the user.

    The object contains both the modern format fields
    (`active_timestamp` and `idle_timestamp`) and the legacy
    format fields (`website` and `aggregated` dictionaries,
    which contain a timestamp and a status string). New
    integrations should use the modern fields; the legacy
    fields are retained for backwards compatibility.

    **Changes**: In Zulip 12.0 (feature level 497),
    the `website` and `aggregated` legacy dictionaries were
    restored alongside the modern fields, for backwards
    compatibility with integrations written against earlier
    versions of the API.

    In Zulip 12.0 (feature level 487), the `active_timestamp`
    and `idle_timestamp` fields were added to this object, and
    the `website` and `aggregated` dictionaries were
    temporarily removed.
    """

    active_timestamp: typing.Optional[int] = pydantic.Field(default=None)
    """
    The UNIX timestamp of the last time a client connected
    to Zulip reported that the user was actually present.
    """

    idle_timestamp: typing.Optional[int] = pydantic.Field(default=None)
    """
    The UNIX timestamp of the last time the user had a
    client connected to Zulip, including idle clients.
    """

    website: GetUserPresenceResponsePresenceWebsite = pydantic.Field()
    """
    Presence details for the user in the legacy format.
    Starting with Zulip 7.0 (feature level 178), the
    `website` and `aggregated` dictionaries always contain
    identical data, since the server no longer stores which
    client submitted presence updates.
    """

    aggregated: GetUserPresenceResponsePresenceAggregated = pydantic.Field()
    """
    Presence details for the user in the legacy format.
    Unlike `website`, the `status` will be `"offline"` if
    the most recent presence update is older than the
    server's offline threshold.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
