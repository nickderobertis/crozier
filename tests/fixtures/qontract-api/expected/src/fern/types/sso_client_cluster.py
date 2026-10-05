

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sso_client_auth import SsoClientAuth


class SsoClientCluster(UniversalBaseModel):
    """
    A single cluster considered for RHIDP, as compiled client-side from OCM labels.

    Sent for ALL rhidp-labeled clusters (not just enabled ones) so the backend can
    expose the rhidp_managed_clusters metric (all discovered clusters per org,
    regardless of status) while only reconciling rhidp_enabled ones.
    """

    auth: SsoClientAuth = pydantic.Field()
    """
    SSO client auth configuration
    """

    console_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Cluster console URL
    """

    name: str = pydantic.Field()
    """
    Cluster name
    """

    organization_id: str = pydantic.Field()
    """
    OCM organization id
    """

    rhidp_enabled: bool = pydantic.Field()
    """
    Whether this cluster should have an SSO client reconciled
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
