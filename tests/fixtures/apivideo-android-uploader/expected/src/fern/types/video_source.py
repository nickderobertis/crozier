

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .video_source_live_stream import VideoSourceLiveStream


class VideoSource(UniversalBaseModel):
    """
    Source information about the video.
    """

    uri: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL where the video is stored.
    """

    type: typing.Optional[str] = None
    live_stream: typing_extensions.Annotated[
        typing.Optional[VideoSourceLiveStream], FieldMetadata(alias="liveStream"), pydantic.Field(alias="liveStream")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
