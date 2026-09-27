

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .motion_request_clip_clip_format import MotionRequestClipClipFormat
from .motion_request_clip_clip_tracks_item import MotionRequestClipClipTracksItem


class MotionRequestClipClip(UniversalBaseModel):
    format: MotionRequestClipClipFormat
    version: float
    name: str
    duration: float
    tracks: typing.List[MotionRequestClipClipTracksItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
