

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1ServiceHealthResponseOutputInfoConnectedCluster(UniversalBaseModel):
    healthy: bool = pydantic.Field()
    """
    Deprecated. Use `status` instead.
    """

    db_connected: bool
    replication_connected: bool
    connected_cluster: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
