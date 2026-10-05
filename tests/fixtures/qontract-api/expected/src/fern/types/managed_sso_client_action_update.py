

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ManagedSsoClientActionUpdate(UniversalBaseModel):
    """
    Action: update an existing managed SSO client's OIDC configuration on Keycloak.

    Keycloak-only - a change to the tenant secret's output path is an
    independent concern, represented by its own ManagedSsoClientActionMoveTenantSecret.
    """

    client_id: str = pydantic.Field()
    """
    Exact Keycloak clientId of the client being updated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
