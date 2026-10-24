

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .proposal_operation import ProposalOperation
from .proposal_payload import ProposalPayload
from .proposal_risk import ProposalRisk


class ProposalVersion(UniversalBaseModel):
    version_id: str
    version: int
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
    expires_at: dt.datetime
    created_by: str
    created_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
