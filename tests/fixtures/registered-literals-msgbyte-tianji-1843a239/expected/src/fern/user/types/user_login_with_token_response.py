

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .user_login_with_token_response_info import UserLoginWithTokenResponseInfo


class UserLoginWithTokenResponse(UniversalBaseModel):
    info: UserLoginWithTokenResponseInfo
    token: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
