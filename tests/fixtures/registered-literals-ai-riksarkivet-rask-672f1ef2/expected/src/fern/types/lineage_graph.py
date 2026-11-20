

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .graph_edge import GraphEdge
from .graph_node import GraphNode


class LineageGraph(UniversalBaseModel):
    """
    The connected lineage subgraph around ``root`` — nodes + edges for a DAG view.

    Mirrors what Marquez's graph endpoint feeds its UI, trimmed to the dataset-level
    ``DERIVED_FROM`` lineage we model.
    """

    edges: typing.List[GraphEdge]
    nodes: typing.List[GraphNode]
    root: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
