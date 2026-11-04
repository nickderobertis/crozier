

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .authorization_code_o_auth_flow import AuthorizationCodeOAuthFlow
from .client_credentials_o_auth_flow import ClientCredentialsOAuthFlow
from .implicit_o_auth_flow import ImplicitOAuthFlow
from .password_o_auth_flow import PasswordOAuthFlow


class OAuthFlows(UniversalBaseModel):
    """
    Defines the configuration for the supported OAuth 2.0 flows.
    """

    authorization_code: typing_extensions.Annotated[
        typing.Optional[AuthorizationCodeOAuthFlow],
        FieldMetadata(alias="authorizationCode"),
        pydantic.Field(alias="authorizationCode"),
    ] = None
    client_credentials: typing_extensions.Annotated[
        typing.Optional[ClientCredentialsOAuthFlow],
        FieldMetadata(alias="clientCredentials"),
        pydantic.Field(alias="clientCredentials"),
    ] = None
    implicit: typing.Optional[ImplicitOAuthFlow] = None
    password: typing.Optional[PasswordOAuthFlow] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
