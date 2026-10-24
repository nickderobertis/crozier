

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .agent_run_origin import AgentRunOrigin
from .agent_run_review_status import AgentRunReviewStatus
from .agent_run_status import AgentRunStatus
from .agent_run_workflow import AgentRunWorkflow
from .evidence_source import EvidenceSource
from .platform_id import PlatformId


class AgentRun(UniversalBaseModel):
    id: str
    tenant_id: str
    idempotency_key: str
    workflow: AgentRunWorkflow
    objective: str
    evidence: typing.Optional[typing.List[EvidenceSource]] = None
    platforms: typing.List[PlatformId]
    requested_by: str
    status: AgentRunStatus
    provider: str
    model: typing.Optional[str] = None
    graph_version_id: typing.Optional[str] = None
    graph_version_hash: typing.Optional[str] = None
    metric_observation_ids: typing.List[str]
    origin: AgentRunOrigin
    parent_daily_ops_run_id: typing.Optional[str] = None
    parent_daily_ops_attempt: typing.Optional[int] = None
    review_status: AgentRunReviewStatus
    attempt_count: int
    error: typing.Optional[str] = None
    created_at: dt.datetime
    updated_at: dt.datetime
    completed_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
