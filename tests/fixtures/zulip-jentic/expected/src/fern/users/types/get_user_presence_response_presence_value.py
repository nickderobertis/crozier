

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetUserPresenceResponsePresenceValue(UniversalBaseModel):
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

    timestamp: typing.Optional[int] = pydantic.Field(default=None)
    """
    When this update was received. If the timestamp
    is more than a few minutes in the past, the user is offline.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Whether the user had recently interacted with Zulip at the time
    of the timestamp.
    
    Will be either `"active"` or `"idle"`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
