

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .function_id_ref import FunctionIdRef
from .graph_node_aggregator_position import GraphNodeAggregatorPosition
from .graph_node_btql_position import GraphNodeBtqlPosition
from .graph_node_function_position import GraphNodeFunctionPosition
from .graph_node_gate_position import GraphNodeGatePosition
from .graph_node_input_position import GraphNodeInputPosition
from .graph_node_literal_position import GraphNodeLiteralPosition
from .graph_node_output_position import GraphNodeOutputPosition
from .graph_node_prompt_template_position import GraphNodePromptTemplatePosition
from .prompt_block_data import PromptBlockData


class GraphNode_Function(UniversalBaseModel):
    type: typing.Literal["function"] = "function"
    description: typing.Optional[str] = None
    position: typing.Optional[GraphNodeFunctionPosition] = None
    function: FunctionIdRef

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GraphNode_Input(UniversalBaseModel):
    type: typing.Literal["input"] = "input"
    description: typing.Optional[str] = None
    position: typing.Optional[GraphNodeInputPosition] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GraphNode_Output(UniversalBaseModel):
    type: typing.Literal["output"] = "output"
    description: typing.Optional[str] = None
    position: typing.Optional[GraphNodeOutputPosition] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GraphNode_Literal(UniversalBaseModel):
    type: typing.Literal["literal"] = "literal"
    description: typing.Optional[str] = None
    position: typing.Optional[GraphNodeLiteralPosition] = None
    value: typing.Optional[typing.Any] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GraphNode_Btql(UniversalBaseModel):
    type: typing.Literal["btql"] = "btql"
    description: typing.Optional[str] = None
    position: typing.Optional[GraphNodeBtqlPosition] = None
    expr: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GraphNode_Gate(UniversalBaseModel):
    type: typing.Literal["gate"] = "gate"
    description: typing.Optional[str] = None
    position: typing.Optional[GraphNodeGatePosition] = None
    condition: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GraphNode_Aggregator(UniversalBaseModel):
    type: typing.Literal["aggregator"] = "aggregator"
    description: typing.Optional[str] = None
    position: typing.Optional[GraphNodeAggregatorPosition] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GraphNode_PromptTemplate(UniversalBaseModel):
    type: typing.Literal["prompt_template"] = "prompt_template"
    description: typing.Optional[str] = None
    position: typing.Optional[GraphNodePromptTemplatePosition] = None
    prompt: PromptBlockData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


GraphNode = typing_extensions.Annotated[
    typing.Union[
        GraphNode_Function,
        GraphNode_Input,
        GraphNode_Output,
        GraphNode_Literal,
        GraphNode_Btql,
        GraphNode_Gate,
        GraphNode_Aggregator,
        GraphNode_PromptTemplate,
    ],
    pydantic.Field(discriminator="type"),
]
