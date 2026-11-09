

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bank_initiated_risk_tier import BankInitiatedRiskTier
from .signal_score import SignalScore


class BankInitiatedReturnRisk(UniversalBaseModel):
    """
    The object contains a risk score and a risk tier that evaluate the transaction return risk because an account is overdrawn or because an ineligible account is used. Common return codes in this category include: "R01", "R02", "R03", "R04", "R06", "R08",  "R09", "R13", "R16", "R17", "R20", "R23". These returns have a turnaround time of 2 banking days.
    """

    risk_tier: BankInitiatedRiskTier
    score: SignalScore

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
