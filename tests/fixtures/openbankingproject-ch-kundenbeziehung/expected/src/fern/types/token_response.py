

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .token_response_token_type import TokenResponseTokenType


class TokenResponse(UniversalBaseModel):
    access_token: str = pydantic.Field()
    """
    JWT access token
    """

    refresh_token: typing.Optional[str] = pydantic.Field(default=None)
    """
    Refresh token for getting new access tokens
    """

    token_type: TokenResponseTokenType = pydantic.Field()
    """
    Token type (Bearer or DPoP)
    """

    expires_in: int = pydantic.Field()
    """
    Token lifetime in seconds
    """

    scope: typing.Optional[str] = pydantic.Field(default=None)
    """
    Granted OAuth scopes
    """

    id_token: typing.Optional[str] = pydantic.Field(default=None)
    """
    OpenID Connect ID token (JWT)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
