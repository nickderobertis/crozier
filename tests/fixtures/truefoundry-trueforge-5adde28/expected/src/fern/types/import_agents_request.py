

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .import_agent_item import ImportAgentItem


class ImportAgentsRequest(UniversalBaseModel):
    agents: typing.List[ImportAgentItem] = pydantic.Field()
    """
    Agents to create; each carries tenant_id and created_by_subject.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
