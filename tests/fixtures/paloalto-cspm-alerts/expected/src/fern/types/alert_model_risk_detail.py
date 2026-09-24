

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .policy_risk_score_model import PolicyRiskScoreModel
from .score_model import ScoreModel


class AlertModelRiskDetail(UniversalBaseModel):
    """
    Risk detail (Deprecated)
    """

    policy_scores: typing_extensions.Annotated[
        typing.Optional[typing.List[PolicyRiskScoreModel]],
        FieldMetadata(alias="policyScores"),
        pydantic.Field(alias="policyScores"),
    ] = None
    rating: typing.Optional[str] = pydantic.Field(default=None)
    """
    Rating
    """

    risk_score: typing_extensions.Annotated[
        typing.Optional[ScoreModel], FieldMetadata(alias="riskScore"), pydantic.Field(alias="riskScore")
    ] = None
    score: typing.Optional[str] = pydantic.Field(default=None)
    """
    Score
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
