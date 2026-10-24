

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .proposal_capability_block import ProposalCapabilityBlock
from .proposal_capability_status import ProposalCapabilityStatus
from .proposal_decision import ProposalDecision
from .proposal_execution import ProposalExecution
from .proposal_operation import ProposalOperation
from .proposal_payload import ProposalPayload
from .proposal_risk import ProposalRisk
from .proposal_status import ProposalStatus
from .proposal_version import ProposalVersion


class Proposal(UniversalBaseModel):
    id: str
    tenant_id: str
    idempotency_key: str
    daily_ops_run_id: str
    agent_run_id: str
    graph_version_id: str
    graph_version_hash: str
    priority_rank: int
    version: int
    version_id: str
    title: str
    rationale: str
    expected_impact: str
    rollback_plan: str
    evidence_refs: typing.List[str]
    metric_observation_ids: typing.List[str]
    operation: ProposalOperation
    payload: ProposalPayload
    payload_hash: str
    content_hash: str
    risk: ProposalRisk
    status: ProposalStatus
    required_approvals: int
    approval_count: int
    created_by: str
    expires_at: dt.datetime
    submitted_at: typing.Optional[dt.datetime] = None
    completed_at: typing.Optional[dt.datetime] = None
    created_at: dt.datetime
    updated_at: dt.datetime
    decisions: typing.List[ProposalDecision]
    executions: typing.List[ProposalExecution]
    versions: typing.List[ProposalVersion]
    capability_block: typing.Optional[ProposalCapabilityBlock] = None
    capability_status: ProposalCapabilityStatus
    capability_reason: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
