

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Introspection(UniversalBaseModel):
    active: typing.Optional[bool] = pydantic.Field(default=None)
    """
    if the token has expired
    """

    client_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    id of client who owns the token
    """

    exp: typing.Optional[str] = pydantic.Field(default=None)
    """
    expiration time in ms
    """

    iat: typing.Optional[str] = pydantic.Field(default=None)
    """
    when the token was issued
    """

    iss: typing.Optional[str] = pydantic.Field(default=None)
    """
    the issuer
    """

    jti: typing.Optional[str] = pydantic.Field(default=None)
    """
    unique string
    """

    scope: typing.Optional[str] = pydantic.Field(default=None)
    """
    scope
    """

    sub: typing.Optional[str] = pydantic.Field(default=None)
    """
    subject of token (not always present, depending on the token)
    """

    token_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    type of token
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
