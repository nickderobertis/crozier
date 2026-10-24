

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .graph_node_expansion import GraphNodeExpansion
from .graph_node_instruction_key import GraphNodeInstructionKey
from .graph_node_key import GraphNodeKey
from .graph_node_role import GraphNodeRole
from .tool_policy import ToolPolicy


class GraphNode(UniversalBaseModel):
    key: GraphNodeKey
    role: GraphNodeRole
    expansion: GraphNodeExpansion
    optional: bool
    skill_ids: typing.List[str]
    instruction_key: GraphNodeInstructionKey
    tool_policy: ToolPolicy

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
