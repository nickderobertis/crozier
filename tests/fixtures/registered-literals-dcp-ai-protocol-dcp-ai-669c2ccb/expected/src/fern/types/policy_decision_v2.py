

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .policy_decision_v2decision import PolicyDecisionV2Decision
from .policy_decision_v2resolved_tier import PolicyDecisionV2ResolvedTier


class PolicyDecisionV2(UniversalBaseModel):
    dcp_version: typing.Optional[str] = None
    intent_id: typing.Optional[str] = None
    session_nonce: typing.Optional[str] = None
    decision: typing.Optional[PolicyDecisionV2Decision] = None
    risk_score: typing.Optional[int] = None
    reasons: typing.Optional[typing.List[str]] = None
    required_confirmation: typing.Optional[typing.Dict[str, typing.Any]] = None
    applied_policy_hash: typing.Optional[str] = None
    timestamp: typing.Optional[dt.datetime] = None
    resolved_tier: typing.Optional[PolicyDecisionV2ResolvedTier] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
