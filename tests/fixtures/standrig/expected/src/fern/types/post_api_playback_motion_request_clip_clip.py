

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_api_playback_motion_request_clip_clip_format import PostApiPlaybackMotionRequestClipClipFormat
from .post_api_playback_motion_request_clip_clip_tracks_item import PostApiPlaybackMotionRequestClipClipTracksItem


class PostApiPlaybackMotionRequestClipClip(UniversalBaseModel):
    format: PostApiPlaybackMotionRequestClipClipFormat
    version: float
    name: str
    duration: float
    tracks: typing.List[PostApiPlaybackMotionRequestClipClipTracksItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
