

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .graph_edge_purpose import GraphEdgePurpose
from .graph_edge_source import GraphEdgeSource
from .graph_edge_target import GraphEdgeTarget


class GraphEdge(UniversalBaseModel):
    source: GraphEdgeSource
    target: GraphEdgeTarget
    purpose: GraphEdgePurpose = pydantic.Field()
    """
    The purpose of the edge
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
