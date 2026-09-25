

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1OAuthIntrospectResponse(UniversalBaseModel):
    active: bool = pydantic.Field()
    """
    Boolean indicator if the token is active
    """

    scope: typing.Optional[str] = pydantic.Field(default=None)
    """
    Space-separated list of scopes
    """

    client_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Client identifier for the OAuth 2.0 client
    """

    username: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human-readable identifier for the resource owner
    """

    token_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Type of the token
    """

    exp: typing.Optional[int] = pydantic.Field(default=None)
    """
    Expiration timestamp (Unix timestamp)
    """

    iat: typing.Optional[int] = pydantic.Field(default=None)
    """
    Token issued at timestamp (Unix timestamp)
    """

    sub: typing.Optional[str] = pydantic.Field(default=None)
    """
    Subject of the token (usually user ID)
    """

    aud: typing.Optional[str] = pydantic.Field(default=None)
    """
    Audience of the token
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
