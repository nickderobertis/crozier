

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .agents_search_deployed_agents_request_search_item_agent_id_operator import (
    AgentsSearchDeployedAgentsRequestSearchItemAgentIdOperator,
)
from .agents_search_deployed_agents_request_search_item_identity_operator import (
    AgentsSearchDeployedAgentsRequestSearchItemIdentityOperator,
)
from .agents_search_deployed_agents_request_search_item_name_operator import (
    AgentsSearchDeployedAgentsRequestSearchItemNameOperator,
)
from .agents_search_deployed_agents_request_search_item_tags_operator import (
    AgentsSearchDeployedAgentsRequestSearchItemTagsOperator,
)
from .agents_search_deployed_agents_request_search_item_template_name_operator import (
    AgentsSearchDeployedAgentsRequestSearchItemTemplateNameOperator,
)


class AgentsSearchDeployedAgentsRequestSearchItem_Version(UniversalBaseModel):
    field: typing.Literal["version"] = "version"
    value: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AgentsSearchDeployedAgentsRequestSearchItem_Name(UniversalBaseModel):
    field: typing.Literal["name"] = "name"
    operator: AgentsSearchDeployedAgentsRequestSearchItemNameOperator
    value: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AgentsSearchDeployedAgentsRequestSearchItem_Tags(UniversalBaseModel):
    field: typing.Literal["tags"] = "tags"
    operator: AgentsSearchDeployedAgentsRequestSearchItemTagsOperator
    value: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AgentsSearchDeployedAgentsRequestSearchItem_Identity(UniversalBaseModel):
    field: typing.Literal["identity"] = "identity"
    operator: AgentsSearchDeployedAgentsRequestSearchItemIdentityOperator
    value: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AgentsSearchDeployedAgentsRequestSearchItem_TemplateName(UniversalBaseModel):
    field: typing.Literal["templateName"] = "templateName"
    operator: AgentsSearchDeployedAgentsRequestSearchItemTemplateNameOperator
    value: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AgentsSearchDeployedAgentsRequestSearchItem_AgentId(UniversalBaseModel):
    field: typing.Literal["agentId"] = "agentId"
    operator: AgentsSearchDeployedAgentsRequestSearchItemAgentIdOperator
    value: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


AgentsSearchDeployedAgentsRequestSearchItem = typing_extensions.Annotated[
    typing.Union[
        AgentsSearchDeployedAgentsRequestSearchItem_Version,
        AgentsSearchDeployedAgentsRequestSearchItem_Name,
        AgentsSearchDeployedAgentsRequestSearchItem_Tags,
        AgentsSearchDeployedAgentsRequestSearchItem_Identity,
        AgentsSearchDeployedAgentsRequestSearchItem_TemplateName,
        AgentsSearchDeployedAgentsRequestSearchItem_AgentId,
    ],
    pydantic.Field(discriminator="field"),
]
