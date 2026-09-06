

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .graph_node_gate_position import GraphNodeGatePosition


class GraphNodeGate(UniversalBaseModel):
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the node
    """

    position: typing.Optional[GraphNodeGatePosition] = pydantic.Field(default=None)
    """
    The position of the node
    """

    condition: typing.Optional[str] = pydantic.Field(default=None)
    """
    A BTQL expression to be evaluated
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
