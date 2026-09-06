

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .graph_node_btql_position import GraphNodeBtqlPosition


class GraphNodeBtql(UniversalBaseModel):
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the node
    """

    position: typing.Optional[GraphNodeBtqlPosition] = pydantic.Field(default=None)
    """
    The position of the node
    """

    expr: str = pydantic.Field()
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
