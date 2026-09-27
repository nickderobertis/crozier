

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_api_playback_motion_request_clip_clip_tracks_item_keys_item_segment import (
    PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegment,
)


class PostApiPlaybackMotionRequestClipClipTracksItemKeysItem(UniversalBaseModel):
    time: float
    value: float
    segment: typing.Optional[PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegment] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
