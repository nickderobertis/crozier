

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .introspection_response_token_type import IntrospectionResponseTokenType


class IntrospectionResponse(UniversalBaseModel):
    active: bool = pydantic.Field()
    """
    Whether the token is active
    """

    client_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Client identifier
    """

    scope: typing.Optional[str] = pydantic.Field(default=None)
    """
    Authorized scopes
    """

    sub: typing.Optional[str] = pydantic.Field(default=None)
    """
    Subject of the token
    """

    aud: typing.Optional[str] = pydantic.Field(default=None)
    """
    Intended audience
    """

    iss: typing.Optional[str] = pydantic.Field(default=None)
    """
    Token issuer
    """

    exp: typing.Optional[int] = pydantic.Field(default=None)
    """
    Expiration time (Unix timestamp)
    """

    iat: typing.Optional[int] = pydantic.Field(default=None)
    """
    Issued at time (Unix timestamp)
    """

    token_type: typing.Optional[IntrospectionResponseTokenType] = pydantic.Field(default=None)
    """
    Token type
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
