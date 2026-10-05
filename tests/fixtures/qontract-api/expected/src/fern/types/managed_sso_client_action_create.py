

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ManagedSsoClientActionCreate(UniversalBaseModel):
    """
    Action: register a new managed SSO client with Keycloak.
    """

    client_id: str = pydantic.Field()
    """
    Exact Keycloak clientId of the client being created.
    """

    tenant_secret_path: str = pydantic.Field()
    """
    Vault path of the tenant-facing credential secret.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
