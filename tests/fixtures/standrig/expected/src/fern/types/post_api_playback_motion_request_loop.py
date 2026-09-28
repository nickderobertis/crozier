

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_api_playback_motion_request_loop_action import PostApiPlaybackMotionRequestLoopAction


class PostApiPlaybackMotionRequestLoop(UniversalBaseModel):
    action: PostApiPlaybackMotionRequestLoopAction
    speed: typing.Optional[float] = None
    loop: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
