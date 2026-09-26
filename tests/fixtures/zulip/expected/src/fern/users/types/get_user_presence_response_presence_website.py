

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_user_presence_response_presence_website_status import GetUserPresenceResponsePresenceWebsiteStatus


class GetUserPresenceResponsePresenceWebsite(UniversalBaseModel):
    """
    Presence details for the user in the legacy format.
    Starting with Zulip 7.0 (feature level 178), the
    `website` and `aggregated` dictionaries always contain
    identical data, since the server no longer stores which
    client submitted presence updates.
    """

    status: typing.Optional[GetUserPresenceResponsePresenceWebsiteStatus] = pydantic.Field(default=None)
    """
    The status of the user. Will be either `"idle"` or
    `"active"`.
    """

    timestamp: typing.Optional[int] = pydantic.Field(default=None)
    """
    The UNIX timestamp of when the user's presence data
    was last updated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
