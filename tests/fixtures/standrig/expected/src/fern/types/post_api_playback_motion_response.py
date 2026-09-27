

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_api_playback_motion_response_playback import PostApiPlaybackMotionResponsePlayback


class PostApiPlaybackMotionResponse(UniversalBaseModel):
    ok: typing.Optional[str] = None
    playback: typing.Optional[PostApiPlaybackMotionResponsePlayback] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
