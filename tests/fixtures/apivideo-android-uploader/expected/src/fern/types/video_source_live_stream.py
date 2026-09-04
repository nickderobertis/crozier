

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .video_source_live_stream_link import VideoSourceLiveStreamLink


class VideoSourceLiveStream(UniversalBaseModel):
    """
    This appears if the video is from a Live Record.
    """

    live_stream_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="liveStreamId"),
        pydantic.Field(alias="liveStreamId", description="The unique identifier for the live stream."),
    ] = None
    """
    The unique identifier for the live stream.
    """

    links: typing.Optional[typing.List[VideoSourceLiveStreamLink]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
