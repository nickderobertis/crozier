

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .proposal_decision_type import ProposalDecisionType


class ProposalDecision(UniversalBaseModel):
    id: str
    tenant_id: str
    proposal_id: str
    proposal_version: int
    content_hash: str
    decision: ProposalDecisionType
    comment: str
    decided_by: str
    created_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
