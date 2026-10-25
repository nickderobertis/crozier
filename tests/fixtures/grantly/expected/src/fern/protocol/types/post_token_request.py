

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PostTokenRequest_AuthorizationCode(UniversalBaseModel):
    grant_type: typing.Literal["authorization_code"] = "authorization_code"
    code: str
    redirect_uri: str
    code_verifier: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PostTokenRequest_RefreshToken(UniversalBaseModel):
    grant_type: typing.Literal["refresh_token"] = "refresh_token"
    refresh_token: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


PostTokenRequest = typing_extensions.Annotated[
    typing.Union[PostTokenRequest_AuthorizationCode, PostTokenRequest_RefreshToken],
    pydantic.Field(discriminator="grant_type"),
]
