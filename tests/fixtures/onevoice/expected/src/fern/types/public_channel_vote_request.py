

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .public_channel_vote_request_channel import PublicChannelVoteRequestChannel


class PublicChannelVoteRequest(UniversalBaseModel):
    """
    Public fake-door vote for a not-yet-supported channel, cast from the
    marketing landing by an unauthenticated visitor. Measures anonymous
    top-of-funnel demand; distinct from the business-scoped
    CreateChannelRequestRequest.
    """

    channel: PublicChannelVoteRequestChannel
    note: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
