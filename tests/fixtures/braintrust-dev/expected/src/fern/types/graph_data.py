

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .graph_data_type import GraphDataType
from .graph_edge import GraphEdge
from .graph_node import GraphNode


class GraphData(UniversalBaseModel):
    """
    This feature is preliminary and unsupported.
    """

    type: GraphDataType
    nodes: typing.Dict[str, GraphNode]
    edges: typing.Dict[str, GraphEdge]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
