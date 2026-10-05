

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ocm_oidc_idp_auth import OcmOidcIdpAuth


class OcmOidcIdpCluster(UniversalBaseModel):
    """
    A single cluster considered for RHIDP OIDC, compiled client-side from OCM labels.

    Sent for every RHIDP-managed cluster (not just oidc_enabled ones), so the current
    state (existing OCM identity providers) can still be diffed and cleaned up for
    clusters that became disabled since the last reconcile.
    """

    auth: OcmOidcIdpAuth = pydantic.Field()
    """
    OIDC auth configuration
    """

    cluster_id: str = pydantic.Field()
    """
    OCM cluster id
    """

    name: str = pydantic.Field()
    """
    Cluster name
    """

    organization_id: str = pydantic.Field()
    """
    OCM organization id
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
