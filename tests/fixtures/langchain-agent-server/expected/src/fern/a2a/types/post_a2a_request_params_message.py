

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_a2a_request_params_message_message import PostA2ARequestParamsMessageMessage


class PostA2ARequestParamsMessage(UniversalBaseModel):
    message: PostA2ARequestParamsMessageMessage

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
