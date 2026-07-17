

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .keycloak_config_ssl_required import KeycloakConfigSslRequired


class KeycloakConfig(UniversalBaseModel):
    """
    Representation of Keycloak / SSO configuration used by Microcks server
    """

    auth_server_url: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="auth-server-url"),
        pydantic.Field(alias="auth-server-url", description="SSO Server authentication url"),
    ]
    """
    SSO Server authentication url
    """

    enabled: bool = pydantic.Field()
    """
    Whether Keycloak authentification and usage is enabled
    """

    public_client: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="public-client"),
        pydantic.Field(
            alias="public-client", description="Name of public-client that can be used for requesting OAuth token"
        ),
    ]
    """
    Name of public-client that can be used for requesting OAuth token
    """

    realm: str = pydantic.Field()
    """
    Authentication realm name
    """

    resource: str = pydantic.Field()
    """
    Name of Keycloak resource/application used on client side
    """

    ssl_required: typing_extensions.Annotated[
        KeycloakConfigSslRequired,
        FieldMetadata(alias="ssl-required"),
        pydantic.Field(alias="ssl-required", description="SSL certificates requirements"),
    ]
    """
    SSL certificates requirements
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
