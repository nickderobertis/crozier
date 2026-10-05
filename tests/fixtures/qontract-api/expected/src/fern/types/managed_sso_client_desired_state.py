

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .keycloak_instance_ref import KeycloakInstanceRef
from .oidc_desired_state import OidcDesiredState
from .secret import Secret


class ManagedSsoClientDesiredState(UniversalBaseModel):
    """
    Desired state for a single managed SSO client.
    """

    client_id: str = pydantic.Field()
    """
    Exact Keycloak clientId, taken as-is
    """

    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether this client is active on Keycloak. Set to False to deactivate it in place (Keycloak rejects logins/tokens for a disabled client) without deleting this object, which would delete the Keycloak registration and its secret entirely.
    """

    keycloak_instance: KeycloakInstanceRef = pydantic.Field()
    """
    The Keycloak realm to register/manage this client against.
    """

    oidc: typing.Optional[OidcDesiredState] = pydantic.Field(default=None)
    """
    OIDC-specific configuration. Required for a working client in this milestone - SAML is not yet supported.
    """

    output: typing.Optional[Secret] = pydantic.Field(default=None)
    """
    Vault path for the tenant-facing credential secret. If None, the reconciler writes to an integration-managed default path.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
