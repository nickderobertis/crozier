

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .graph_edge import GraphEdge
from .graph_node import GraphNode


class AgentGraphDefinition(UniversalBaseModel):
    schema_version: int
    nodes: typing.List[GraphNode]
    edges: typing.List[GraphEdge]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
