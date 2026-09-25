

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .legacy_presence_format_status import LegacyPresenceFormatStatus


class LegacyPresenceFormat(UniversalBaseModel):
    """
    `{client_name}` or `"aggregated"`: Object containing the details of the user's
    presence.

    **Changes**: Starting with Zulip 7.0 (feature level 178), this will always
    contain two keys, `"website"` and `"aggregated"`, with identical data. The
    server no longer stores which client submitted presence updates.

    Previously, the `{client_name}` keys for these objects were the names of the
    different clients where the user was logged in, for example `website` or
    `ZulipDesktop`.
    """

    client: typing.Optional[str] = pydantic.Field(default=None)
    """
    The client's platform name.
    
    **Changes**: Starting with Zulip 7.0 (feature level 178), this will
    always be `"website"` as the server no longer stores which client
    submitted presence data.
    """

    status: typing.Optional[LegacyPresenceFormatStatus] = pydantic.Field(default=None)
    """
    The status of the user on this client. Will be either `"idle"`
    or `"active"`.
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
    
    Not present in objects with the `"aggregated"` key.
    
    **Changes**: Starting with Zulip 7.0 (feature level 178), always
    `false` when present as the server no longer stores which client
    submitted presence data.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
