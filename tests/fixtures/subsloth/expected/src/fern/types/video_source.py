

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .resolution_label import ResolutionLabel
from .video_source_type import VideoSourceType


class VideoSource(UniversalBaseModel):
    """
    A single video stream source with URL, resolution, quality, and MIME type.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Subtitle URL. May be signed; never persist in fixtures, database, preferences, diagnostics, or logs.
    """

    download_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Subtitle download URL. May be signed; never persist in fixtures, database, preferences, diagnostics, or logs.
    """

    resolution: typing.Optional[ResolutionLabel] = None
    quality: typing.Optional[ResolutionLabel] = None
    mime_type: typing.Optional[str] = None
    type: typing.Optional[VideoSourceType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
