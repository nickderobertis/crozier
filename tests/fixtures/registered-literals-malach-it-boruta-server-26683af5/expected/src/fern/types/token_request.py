

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .token_request_grant_type import TokenRequestGrantType


class TokenRequest(UniversalBaseModel):
    grant_type: TokenRequestGrantType
    code: typing.Optional[str] = None
    redirect_uri: typing.Optional[str] = None
    code_verifier: typing.Optional[str] = None
    refresh_token: typing.Optional[str] = None
    username: typing.Optional[str] = None
    password: typing.Optional[str] = None
    scope: typing.Optional[str] = None
    client_id: typing.Optional[str] = None
    client_secret: typing.Optional[str] = None
    client_assertion_type: typing.Optional[str] = None
    client_assertion: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
