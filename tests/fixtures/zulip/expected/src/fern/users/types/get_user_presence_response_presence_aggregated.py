

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_user_presence_response_presence_aggregated_status import GetUserPresenceResponsePresenceAggregatedStatus


class GetUserPresenceResponsePresenceAggregated(UniversalBaseModel):
    """
    Presence details for the user in the legacy format.
    Unlike `website`, the `status` will be `"offline"` if
    the most recent presence update is older than the
    server's offline threshold.
    """

    status: typing.Optional[GetUserPresenceResponsePresenceAggregatedStatus] = pydantic.Field(default=None)
    """
    The status of the user. Will be either `"idle"`,
    `"active"`, or `"offline"`.
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
