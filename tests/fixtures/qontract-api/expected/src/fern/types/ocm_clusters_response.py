

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ocm_cluster_info import OcmClusterInfo


class OcmClustersResponse(UniversalBaseModel):
    """
    Response model for the cluster discovery endpoint.
    """

    clusters: typing.Optional[typing.List[OcmClusterInfo]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
