

import typing

from .motion_request_clip_clip_tracks_item_keys_item_segment_control1 import (
    MotionRequestClipClipTracksItemKeysItemSegmentControl1,
)
from .motion_request_clip_clip_tracks_item_keys_item_segment_zero import (
    MotionRequestClipClipTracksItemKeysItemSegmentZero,
)

MotionRequestClipClipTracksItemKeysItemSegment = typing.Union[
    MotionRequestClipClipTracksItemKeysItemSegmentZero, MotionRequestClipClipTracksItemKeysItemSegmentControl1
]
