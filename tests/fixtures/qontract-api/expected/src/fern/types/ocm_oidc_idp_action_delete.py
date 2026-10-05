

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OcmOidcIdpActionDelete(UniversalBaseModel):
    """
    Action: delete an identity provider from a cluster.
    """

    cluster_name: str = pydantic.Field()
    """
    Cluster name
    """

    idp_name: str = pydantic.Field()
    """
    Identity provider name
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
