

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_api_playback_motion_request_clip_clip_tracks_item_keys_item_segment_control1control1 import (
    PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegmentControl1Control1,
)
from .post_api_playback_motion_request_clip_clip_tracks_item_keys_item_segment_control1control2 import (
    PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegmentControl1Control2,
)
from .post_api_playback_motion_request_clip_clip_tracks_item_keys_item_segment_control1kind import (
    PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegmentControl1Kind,
)


class PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegmentControl1(UniversalBaseModel):
    kind: PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegmentControl1Kind
    control1: PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegmentControl1Control1
    control2: PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegmentControl1Control2

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
