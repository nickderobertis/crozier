

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_api_playback_motion_request_clip_action import PostApiPlaybackMotionRequestClipAction
from .post_api_playback_motion_request_clip_clip import PostApiPlaybackMotionRequestClipClip


class PostApiPlaybackMotionRequestClip(UniversalBaseModel):
    action: PostApiPlaybackMotionRequestClipAction
    clip: PostApiPlaybackMotionRequestClipClip

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
