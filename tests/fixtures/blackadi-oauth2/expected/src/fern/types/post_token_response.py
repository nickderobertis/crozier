

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_token_response_token_type import PostTokenResponseTokenType


class PostTokenResponse(UniversalBaseModel):
    access_token: typing.Optional[str] = None
    token_type: typing.Optional[PostTokenResponseTokenType] = None
    expires_in: typing.Optional[int] = None
    refresh_token: typing.Optional[str] = None
    id_token: typing.Optional[str] = None
    scope: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
