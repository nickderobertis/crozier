

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .risk_check_behavior_bot_detected_label import RiskCheckBehaviorBotDetectedLabel
from .risk_check_behavior_fraud_ring_detected_label import RiskCheckBehaviorFraudRingDetectedLabel
from .risk_check_behavior_user_interactions_label import RiskCheckBehaviorUserInteractionsLabel


class RiskCheckBehavior(UniversalBaseModel):
    """
    Result summary object specifying values for `behavior` attributes of risk check, when available.
    """

    bot_detected: RiskCheckBehaviorBotDetectedLabel
    fraud_ring_detected: RiskCheckBehaviorFraudRingDetectedLabel
    user_interactions: RiskCheckBehaviorUserInteractionsLabel

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
