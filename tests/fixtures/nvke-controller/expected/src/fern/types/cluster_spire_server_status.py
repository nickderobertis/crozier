

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .node_spire_agent_status import NodeSpireAgentStatus
from .spire_server import SpireServer


class ClusterSpireServerStatus(UniversalBaseModel):
    """
    Requested SPIRE server and live per-node SPIRE agent status.
    """

    requested: typing.Optional[SpireServer] = pydantic.Field(default=None)
    """
    The server last requested. Absent if none was requested.
    """

    nodes: typing.List[NodeSpireAgentStatus] = pydantic.Field()
    """
    Every node of the cluster.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
