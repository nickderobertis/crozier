

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OcmOidcIdpActionCreate(UniversalBaseModel):
    """
    Action: create a new OIDC identity provider on a cluster.
    """

    auth_name: str = pydantic.Field()
    """
    Identity provider name
    """

    cluster_name: str = pydantic.Field()
    """
    Cluster name
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
