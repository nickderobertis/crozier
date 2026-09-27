

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .motion_clip_tracks_item_keys_item_segment_control1control1 import (
    MotionClipTracksItemKeysItemSegmentControl1Control1,
)
from .motion_clip_tracks_item_keys_item_segment_control1control2 import (
    MotionClipTracksItemKeysItemSegmentControl1Control2,
)
from .motion_clip_tracks_item_keys_item_segment_control1kind import MotionClipTracksItemKeysItemSegmentControl1Kind


class MotionClipTracksItemKeysItemSegmentControl1(UniversalBaseModel):
    kind: MotionClipTracksItemKeysItemSegmentControl1Kind
    control1: MotionClipTracksItemKeysItemSegmentControl1Control1
    control2: MotionClipTracksItemKeysItemSegmentControl1Control2

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
