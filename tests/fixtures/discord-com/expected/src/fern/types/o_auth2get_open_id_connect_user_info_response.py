

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OAuth2GetOpenIdConnectUserInfoResponse(UniversalBaseModel):
    sub: str
    email: typing.Optional[str] = None
    email_verified: typing.Optional[bool] = None
    preferred_username: typing.Optional[str] = None
    nickname: typing.Optional[str] = None
    picture: typing.Optional[str] = None
    locale: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
