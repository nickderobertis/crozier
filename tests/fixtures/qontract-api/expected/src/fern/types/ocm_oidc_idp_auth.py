

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OcmOidcIdpAuth(UniversalBaseModel):
    """
    Auth configuration for a cluster's OIDC identity provider.

    Label interpretation stays client-side (see reconcile/rhidp_api/ocm_oidc_idp) -
    oidc_enabled/enforced are booleans computed from OCM labels by the client, not the
    raw StatusValue enum, so this service has zero knowledge of label semantics.
    """

    enforced: bool = pydantic.Field()
    """
    If True, ALL foreign identity providers on this cluster are removed, not just ones matching this auth name
    """

    group_filter_regex: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional group filter regex for the SSO client
    """

    issuer: str = pydantic.Field()
    """
    Keycloak instance URL (must match the stored SSO secret)
    """

    name: str = pydantic.Field()
    """
    IDP name, must match the SSO client auth name
    """

    oidc_enabled: bool = pydantic.Field()
    """
    Whether an OIDC identity provider should exist for this cluster
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
