

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .risk_profile_esg_preferences import RiskProfileEsgPreferences
from .risk_profile_investment_experience import RiskProfileInvestmentExperience
from .risk_profile_investment_horizon import RiskProfileInvestmentHorizon
from .risk_profile_investment_knowledge import RiskProfileInvestmentKnowledge
from .risk_profile_investment_objectives_item import RiskProfileInvestmentObjectivesItem
from .risk_profile_risk_tolerance import RiskProfileRiskTolerance


class RiskProfile(UniversalBaseModel):
    investment_experience: typing_extensions.Annotated[
        typing.Optional[RiskProfileInvestmentExperience],
        FieldMetadata(alias="investmentExperience"),
        pydantic.Field(alias="investmentExperience"),
    ] = None
    investment_knowledge: typing_extensions.Annotated[
        typing.Optional[RiskProfileInvestmentKnowledge],
        FieldMetadata(alias="investmentKnowledge"),
        pydantic.Field(alias="investmentKnowledge"),
    ] = None
    risk_tolerance: typing_extensions.Annotated[
        typing.Optional[RiskProfileRiskTolerance],
        FieldMetadata(alias="riskTolerance"),
        pydantic.Field(alias="riskTolerance"),
    ] = None
    investment_horizon: typing_extensions.Annotated[
        typing.Optional[RiskProfileInvestmentHorizon],
        FieldMetadata(alias="investmentHorizon"),
        pydantic.Field(alias="investmentHorizon"),
    ] = None
    investment_objectives: typing_extensions.Annotated[
        typing.Optional[typing.List[RiskProfileInvestmentObjectivesItem]],
        FieldMetadata(alias="investmentObjectives"),
        pydantic.Field(alias="investmentObjectives"),
    ] = None
    esg_preferences: typing_extensions.Annotated[
        typing.Optional[RiskProfileEsgPreferences],
        FieldMetadata(alias="esgPreferences"),
        pydantic.Field(alias="esgPreferences"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
