

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .token_create_grant_type import TokenCreateGrantType


class TokenCreate(UniversalBaseModel):
    client_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of client to request token for. Leave off if client ID and secret are being supplied through Authorization header.
    """

    client_secret: typing.Optional[str] = pydantic.Field(default=None)
    """
    Leave off if client ID and secret are being supplied through Authorization header.
    """

    code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Authorization code to request token for. Required if grant_type is authorization_code.
    """

    code_verifier: typing.Optional[str] = pydantic.Field(default=None)
    """
    Code verifier to request token for. Only required if code_verifier is provided in the authorization code request.
    """

    grant_type: TokenCreateGrantType
    redirect_uri: typing.Optional[str] = pydantic.Field(default=None)
    """
    Redirect URI to request token for. Required if grant_type is authorization_code.
    """

    state: typing.Optional[str] = pydantic.Field(default=None)
    """
    State to request token for. Only required if state is provided in the authorization code request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
