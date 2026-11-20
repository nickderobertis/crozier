

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .graph_edge import GraphEdge
from .graph_node import GraphNode


class EstateGraph(UniversalBaseModel):
    """
    The whole visible lineage graph in one response — the graph page's bulk read.

    ``total`` is the full visible node count; when it exceeds the requested limit the node list
    is truncated and ``capped`` says so, so a UI can render "N of M" honestly instead of
    pretending the window is the estate.
    """

    capped: typing.Optional[bool] = None
    edges: typing.List[GraphEdge]
    nodes: typing.List[GraphNode]
    total: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
