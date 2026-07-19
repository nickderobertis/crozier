

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .templates_get_template_snapshot_response_agents_item_agent_type import (
    TemplatesGetTemplateSnapshotResponseAgentsItemAgentType,
)
from .templates_get_template_snapshot_response_agents_item_memory_variables import (
    TemplatesGetTemplateSnapshotResponseAgentsItemMemoryVariables,
)
from .templates_get_template_snapshot_response_agents_item_properties import (
    TemplatesGetTemplateSnapshotResponseAgentsItemProperties,
)
from .templates_get_template_snapshot_response_agents_item_tool_rules_item import (
    TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItem,
)
from .templates_get_template_snapshot_response_agents_item_tool_variables import (
    TemplatesGetTemplateSnapshotResponseAgentsItemToolVariables,
)


class TemplatesGetTemplateSnapshotResponseAgentsItem(UniversalBaseModel):
    model: str
    system_prompt: typing_extensions.Annotated[
        str, FieldMetadata(alias="systemPrompt"), pydantic.Field(alias="systemPrompt")
    ]
    tool_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="toolIds"), pydantic.Field(alias="toolIds")
    ] = None
    source_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="sourceIds"), pydantic.Field(alias="sourceIds")
    ] = None
    memory_variables: typing_extensions.Annotated[
        typing.Optional[TemplatesGetTemplateSnapshotResponseAgentsItemMemoryVariables],
        FieldMetadata(alias="memoryVariables"),
        pydantic.Field(alias="memoryVariables"),
    ] = None
    tool_variables: typing_extensions.Annotated[
        typing.Optional[TemplatesGetTemplateSnapshotResponseAgentsItemToolVariables],
        FieldMetadata(alias="toolVariables"),
        pydantic.Field(alias="toolVariables"),
    ] = None
    tags: typing.Optional[typing.List[str]] = None
    identity_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="identityIds"), pydantic.Field(alias="identityIds")
    ] = None
    tool_rules: typing_extensions.Annotated[
        typing.Optional[typing.List[TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItem]],
        FieldMetadata(alias="toolRules"),
        pydantic.Field(alias="toolRules"),
    ] = None
    agent_type: typing_extensions.Annotated[
        TemplatesGetTemplateSnapshotResponseAgentsItemAgentType,
        FieldMetadata(alias="agentType"),
        pydantic.Field(alias="agentType"),
    ]
    properties: typing.Optional[TemplatesGetTemplateSnapshotResponseAgentsItemProperties] = None
    entity_id: typing_extensions.Annotated[str, FieldMetadata(alias="entityId"), pydantic.Field(alias="entityId")]
    name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
