

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .templates_get_template_snapshot_response_agents_item_tool_rules_item_constrain_child_tools_child_arg_nodes_item import (
    TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItemConstrainChildToolsChildArgNodesItem,
)


class TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItemConstrainChildTools(UniversalBaseModel):
    tool_name: str
    prompt_template: typing.Optional[str] = None
    children: typing.List[str]
    child_arg_nodes: typing.Optional[
        typing.List[TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItemConstrainChildToolsChildArgNodesItem]
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
