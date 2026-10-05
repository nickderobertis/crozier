

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ManagedSsoClientActionMoveTenantSecret(UniversalBaseModel):
    """
    Action: migrate the tenant secret to a newly-resolved output path.

    Pure Vault bookkeeping - reuses the client_secret Keycloak already
    issued, no Keycloak call involved. Independent of, and may co-occur
    with, ManagedSsoClientActionUpdate.
    """

    client_id: str = pydantic.Field()
    """
    Exact Keycloak clientId of the client whose tenant secret is moving.
    """

    tenant_secret_path: str = pydantic.Field()
    """
    New Vault path of the tenant-facing credential secret.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
