

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .function_id_ref import FunctionIdRef
from .graph_node_function_position import GraphNodeFunctionPosition


class GraphNodeFunction(UniversalBaseModel):
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the node
    """

    position: typing.Optional[GraphNodeFunctionPosition] = pydantic.Field(default=None)
    """
    The position of the node
    """

    function: FunctionIdRef

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
