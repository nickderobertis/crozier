

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .agents_search_deployed_agents_request_search_item_template_name_operator import (
    AgentsSearchDeployedAgentsRequestSearchItemTemplateNameOperator,
)


class AgentsSearchDeployedAgentsRequestSearchItemTemplateName(UniversalBaseModel):
    operator: AgentsSearchDeployedAgentsRequestSearchItemTemplateNameOperator
    value: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
