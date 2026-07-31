

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LiveVideoToVideoResponse(UniversalBaseModel):
    """
    Response model for live video-to-video generation.
    """

    subscribe_url: str = pydantic.Field()
    """
    Source URL of the incoming stream to subscribe to
    """

    publish_url: str = pydantic.Field()
    """
    Destination URL of the outgoing stream to publish to
    """

    control_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL for updating the live video-to-video generation
    """

    events_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL for subscribing to events for pipeline status and logs
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
