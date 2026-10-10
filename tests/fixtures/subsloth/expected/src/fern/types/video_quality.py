

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .resolution_label import ResolutionLabel


class VideoQuality(UniversalBaseModel):
    """
    Video quality variant with resolution, bitrate, dimensions, and playback URL.
    """

    label: typing.Optional[ResolutionLabel] = None
    resolution: typing.Optional[ResolutionLabel] = None
    url: typing.Optional[str] = None
    width: typing.Optional[int] = None
    height: typing.Optional[int] = None
    bitrate: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
