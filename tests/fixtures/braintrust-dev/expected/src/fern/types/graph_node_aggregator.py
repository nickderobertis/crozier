

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .graph_node_aggregator_position import GraphNodeAggregatorPosition


class GraphNodeAggregator(UniversalBaseModel):
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the node
    """

    position: typing.Optional[GraphNodeAggregatorPosition] = pydantic.Field(default=None)
    """
    The position of the node
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
