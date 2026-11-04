

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .agent_spec import AgentSpec
from .import_agent_item_created_by_subject import ImportAgentItemCreatedBySubject
from .resource_name import ResourceName


class ImportAgentItem(UniversalBaseModel):
    created_by_subject: ImportAgentItemCreatedBySubject = pydantic.Field()
    """
    Original creator to persist on the agent.
    """

    description: typing.Optional[str] = None
    manifest: AgentSpec
    name: ResourceName
    tenant_id: str = pydantic.Field()
    """
    Tenant to create the agent under.
    """

    truefoundry_managed_agent_id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
