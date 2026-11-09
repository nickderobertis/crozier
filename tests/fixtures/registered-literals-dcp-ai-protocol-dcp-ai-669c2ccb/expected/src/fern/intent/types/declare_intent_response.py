

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.policy_decision_v2 import PolicyDecisionV2
from .declare_intent_response_security_tier import DeclareIntentResponseSecurityTier
from .declare_intent_response_verification_mode import DeclareIntentResponseVerificationMode


class DeclareIntentResponse(UniversalBaseModel):
    ok: typing.Optional[bool] = None
    policy_decision: typing.Optional[PolicyDecisionV2] = None
    security_tier: typing.Optional[DeclareIntentResponseSecurityTier] = None
    verification_mode: typing.Optional[DeclareIntentResponseVerificationMode] = None
    checkpoint_interval: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
