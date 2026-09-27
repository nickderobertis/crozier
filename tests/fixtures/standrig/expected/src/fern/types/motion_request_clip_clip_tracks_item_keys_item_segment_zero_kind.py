

import typing

from .motion_request_clip_clip_tracks_item_keys_item_segment_zero_kind_one import (
    MotionRequestClipClipTracksItemKeysItemSegmentZeroKindOne,
)
from .motion_request_clip_clip_tracks_item_keys_item_segment_zero_kind_two import (
    MotionRequestClipClipTracksItemKeysItemSegmentZeroKindTwo,
)
from .motion_request_clip_clip_tracks_item_keys_item_segment_zero_kind_zero import (
    MotionRequestClipClipTracksItemKeysItemSegmentZeroKindZero,
)

MotionRequestClipClipTracksItemKeysItemSegmentZeroKind = typing.Union[
    MotionRequestClipClipTracksItemKeysItemSegmentZeroKindZero,
    MotionRequestClipClipTracksItemKeysItemSegmentZeroKindOne,
    MotionRequestClipClipTracksItemKeysItemSegmentZeroKindTwo,
]
