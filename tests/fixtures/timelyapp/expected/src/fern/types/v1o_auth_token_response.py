

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1OAuthTokenResponse(UniversalBaseModel):
    access_token: str = pydantic.Field()
    """
    OAuth 2.0 access token
    """

    token_type: str = pydantic.Field()
    """
    Token type (always Bearer)
    """

    expires_in: typing.Optional[int] = pydantic.Field(default=None)
    """
    Token expiration time in seconds (null for non-expiring tokens)
    """

    refresh_token: typing.Optional[str] = pydantic.Field(default=None)
    """
    OAuth 2.0 refresh token (if applicable)
    """

    scope: str = pydantic.Field()
    """
    OAuth 2.0 scope
    """

    created_at: int = pydantic.Field()
    """
    Token creation timestamp (Unix timestamp)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
