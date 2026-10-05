

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OcmGroupsCluster(UniversalBaseModel):
    """
    A cluster with its OCM cluster ID and managed groups, sent by the client.
    """

    cluster_id: str = pydantic.Field()
    """
    OCM cluster ID
    """

    managed_groups: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Group names managed on this cluster (e.g. dedicated-admins)
    """

    name: str = pydantic.Field()
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
