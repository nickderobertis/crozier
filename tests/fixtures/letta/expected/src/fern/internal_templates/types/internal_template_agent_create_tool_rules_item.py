

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.tool_call_node import ToolCallNode


class InternalTemplateAgentCreateToolRulesItem_Conditional(UniversalBaseModel):
    type: typing.Literal["conditional"] = "conditional"
    tool_name: str
    prompt_template: typing.Optional[str] = None
    default_child: typing.Optional[str] = None
    child_output_mapping: typing.Dict[str, str]
    require_output_mapping: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class InternalTemplateAgentCreateToolRulesItem_ConstrainChildTools(UniversalBaseModel):
    type: typing.Literal["constrain_child_tools"] = "constrain_child_tools"
    tool_name: str
    prompt_template: typing.Optional[str] = None
    children: typing.List[str]
    child_arg_nodes: typing.Optional[typing.List[ToolCallNode]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class InternalTemplateAgentCreateToolRulesItem_ContinueLoop(UniversalBaseModel):
    type: typing.Literal["continue_loop"] = "continue_loop"
    tool_name: str
    prompt_template: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class InternalTemplateAgentCreateToolRulesItem_ExitLoop(UniversalBaseModel):
    type: typing.Literal["exit_loop"] = "exit_loop"
    tool_name: str
    prompt_template: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class InternalTemplateAgentCreateToolRulesItem_MaxCountPerStep(UniversalBaseModel):
    type: typing.Literal["max_count_per_step"] = "max_count_per_step"
    tool_name: str
    prompt_template: typing.Optional[str] = None
    max_count_limit: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class InternalTemplateAgentCreateToolRulesItem_ParentLastTool(UniversalBaseModel):
    type: typing.Literal["parent_last_tool"] = "parent_last_tool"
    tool_name: str
    prompt_template: typing.Optional[str] = None
    children: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class InternalTemplateAgentCreateToolRulesItem_RequiredBeforeExit(UniversalBaseModel):
    type: typing.Literal["required_before_exit"] = "required_before_exit"
    tool_name: str
    prompt_template: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class InternalTemplateAgentCreateToolRulesItem_RequiresApproval(UniversalBaseModel):
    type: typing.Literal["requires_approval"] = "requires_approval"
    tool_name: str
    prompt_template: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class InternalTemplateAgentCreateToolRulesItem_RunFirst(UniversalBaseModel):
    type: typing.Literal["run_first"] = "run_first"
    tool_name: str
    prompt_template: typing.Optional[str] = None
    args: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


InternalTemplateAgentCreateToolRulesItem = typing_extensions.Annotated[
    typing.Union[
        InternalTemplateAgentCreateToolRulesItem_Conditional,
        InternalTemplateAgentCreateToolRulesItem_ConstrainChildTools,
        InternalTemplateAgentCreateToolRulesItem_ContinueLoop,
        InternalTemplateAgentCreateToolRulesItem_ExitLoop,
        InternalTemplateAgentCreateToolRulesItem_MaxCountPerStep,
        InternalTemplateAgentCreateToolRulesItem_ParentLastTool,
        InternalTemplateAgentCreateToolRulesItem_RequiredBeforeExit,
        InternalTemplateAgentCreateToolRulesItem_RequiresApproval,
        InternalTemplateAgentCreateToolRulesItem_RunFirst,
    ],
    pydantic.Field(discriminator="type"),
]
