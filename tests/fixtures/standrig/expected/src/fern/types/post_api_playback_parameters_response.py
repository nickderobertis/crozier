

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_api_playback_parameters_response_playback import PostApiPlaybackParametersResponsePlayback


class PostApiPlaybackParametersResponse(UniversalBaseModel):
    ok: str
    playback: PostApiPlaybackParametersResponsePlayback

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
