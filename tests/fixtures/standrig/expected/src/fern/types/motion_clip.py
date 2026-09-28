

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .motion_clip_format import MotionClipFormat
from .motion_clip_tracks_item import MotionClipTracksItem


class MotionClip(UniversalBaseModel):
    format: MotionClipFormat
    version: float
    name: str
    duration: float
    tracks: typing.List[MotionClipTracksItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
