

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .motion_clip_tracks_item_keys_item_segment import MotionClipTracksItemKeysItemSegment


class MotionClipTracksItemKeysItem(UniversalBaseModel):
    time: float
    value: float
    segment: typing.Optional[MotionClipTracksItemKeysItemSegment] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
