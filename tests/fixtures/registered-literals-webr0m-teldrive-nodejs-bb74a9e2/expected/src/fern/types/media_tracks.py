

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .media_format import MediaFormat
from .media_track import MediaTrack


class MediaTracks(UniversalBaseModel):
    format: typing.Optional[MediaFormat] = None
    available: bool
    tracks: typing.List[MediaTrack]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
