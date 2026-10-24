

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .agent_task_role import AgentTaskRole
from .agent_task_status import AgentTaskStatus
from .tool_policy import ToolPolicy


class AgentTask(UniversalBaseModel):
    id: str
    tenant_id: str
    run_id: str
    agent_name: str
    graph_node_key: typing.Optional[str] = None
    role: typing.Optional[AgentTaskRole] = None
    tool_policy: ToolPolicy
    skill_ids: typing.List[str]
    status: AgentTaskStatus
    attempt_count: int
    error: typing.Optional[str] = None
    created_at: dt.datetime
    started_at: typing.Optional[dt.datetime] = None
    completed_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
