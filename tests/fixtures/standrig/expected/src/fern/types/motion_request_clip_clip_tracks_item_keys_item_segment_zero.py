

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .motion_request_clip_clip_tracks_item_keys_item_segment_zero_kind import (
    MotionRequestClipClipTracksItemKeysItemSegmentZeroKind,
)


class MotionRequestClipClipTracksItemKeysItemSegmentZero(UniversalBaseModel):
    kind: MotionRequestClipClipTracksItemKeysItemSegmentZeroKind

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
