

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .agent_graph_definition import AgentGraphDefinition
from .agent_graph_version_status import AgentGraphVersionStatus


class AgentGraphVersion(UniversalBaseModel):
    id: str
    graph_id: str
    tenant_id: str
    version: int
    definition_hash: str
    execution_contract_hash: str
    status: AgentGraphVersionStatus
    definition: AgentGraphDefinition
    created_by: str
    created_at: dt.datetime
    published_at: typing.Optional[dt.datetime] = None
    retired_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
