

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .o_auth2token_response_token_type import OAuth2TokenResponseTokenType


class OAuth2TokenResponse(UniversalBaseModel):
    access_token: str = pydantic.Field()
    """
    The access token issued by the authorization server.
    Used to access protected resources on behalf of the user.
    """

    token_type: OAuth2TokenResponseTokenType = pydantic.Field()
    """
    Token type (always "Bearer" for this implementation)
    """

    expires_in: typing.Optional[int] = pydantic.Field(default=None)
    """
    Lifetime of access token in seconds.
    Example: 3600 seconds = 1 hour
    """

    refresh_token: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional refresh token for obtaining new access tokens.
    Used when access token expires.
    """

    scope: typing.Optional[str] = pydantic.Field(default=None)
    """
    Granted scopes.
    Space-separated list of scopes if different from requested.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
