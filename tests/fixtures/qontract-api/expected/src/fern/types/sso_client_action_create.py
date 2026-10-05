

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SsoClientActionCreate(UniversalBaseModel):
    """
    Action: register a new SSO client with Keycloak and store its secret.
    """

    auth_name: str = pydantic.Field()
    """
    Auth name
    """

    cluster_name: str = pydantic.Field()
    """
    Cluster name
    """

    sso_client_id: str = pydantic.Field()
    """
    Vault secret id / Keycloak client id
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
