

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .graph_node_literal_position import GraphNodeLiteralPosition


class GraphNodeLiteral(UniversalBaseModel):
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the node
    """

    position: typing.Optional[GraphNodeLiteralPosition] = pydantic.Field(default=None)
    """
    The position of the node
    """

    value: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    A literal value to be returned
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
