

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ModernPresenceFormat(UniversalBaseModel):
    """
    `{user_id}`: Presence data (modern format) for the user with
    the specified ID.
    """

    active_timestamp: typing.Optional[int] = pydantic.Field(default=None)
    """
    The UNIX timestamp of the last time a client connected
    to Zulip reported that the user was actually present
    (e.g. via focusing a browser window or interacting
    with a computer running the desktop app).
    
    Clients should display users with a current
    `active_timestamp` as fully present.
    """

    idle_timestamp: typing.Optional[int] = pydantic.Field(default=None)
    """
    The UNIX timestamp of the last time the user had a
    client connected to Zulip, including idle clients
    where the user hasn't interacted with the system
    recently.
    
    The Zulip server has no way of distinguishing whether
    an idle web app user is at their computer, but hasn't
    interacted with the Zulip tab recently, or simply left
    their desktop computer on when they left.
    
    Thus, clients should display users with a current
    `idle_timestamp` but no current `active_timestamp` as
    potentially present.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
