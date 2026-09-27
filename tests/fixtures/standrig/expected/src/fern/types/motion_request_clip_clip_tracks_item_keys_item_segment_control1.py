

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .motion_request_clip_clip_tracks_item_keys_item_segment_control1control1 import (
    MotionRequestClipClipTracksItemKeysItemSegmentControl1Control1,
)
from .motion_request_clip_clip_tracks_item_keys_item_segment_control1control2 import (
    MotionRequestClipClipTracksItemKeysItemSegmentControl1Control2,
)
from .motion_request_clip_clip_tracks_item_keys_item_segment_control1kind import (
    MotionRequestClipClipTracksItemKeysItemSegmentControl1Kind,
)


class MotionRequestClipClipTracksItemKeysItemSegmentControl1(UniversalBaseModel):
    kind: MotionRequestClipClipTracksItemKeysItemSegmentControl1Kind
    control1: MotionRequestClipClipTracksItemKeysItemSegmentControl1Control1
    control2: MotionRequestClipClipTracksItemKeysItemSegmentControl1Control2

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
