

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .possible_norm_judge_score_constituents import PossibleNormJudgeScoreConstituents


class PossibleNormJudge(UniversalBaseModel):
    associated_norm_attorneys_api: typing_extensions.Annotated[
        str, FieldMetadata(alias="associatedNormAttorneysAPI"), pydantic.Field(alias="associatedNormAttorneysAPI")
    ]
    associated_norm_law_firms_api: typing_extensions.Annotated[
        str, FieldMetadata(alias="associatedNormLawFirmsAPI"), pydantic.Field(alias="associatedNormLawFirmsAPI")
    ]
    associated_norm_parties_api: typing_extensions.Annotated[
        str, FieldMetadata(alias="associatedNormPartiesAPI"), pydantic.Field(alias="associatedNormPartiesAPI")
    ]
    best_match: typing_extensions.Annotated[bool, FieldMetadata(alias="bestMatch"), pydantic.Field(alias="bestMatch")]
    case_count_analytics_by_norm_judge_api: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="caseCountAnalyticsByNormJudgeAPI"),
        pydantic.Field(alias="caseCountAnalyticsByNormJudgeAPI"),
    ]
    confidence_score: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="confidenceScore"), pydantic.Field(alias="confidenceScore")
    ] = None
    norm_judge_api: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="normJudgeAPI"),
        pydantic.Field(alias="normJudgeAPI", description="Link to Details For the Judge."),
    ]
    """
    Link to Details For the Judge.
    """

    norm_judge_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="normJudgeId"), pydantic.Field(alias="normJudgeId")
    ]
    norm_judge_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="normJudgeName"), pydantic.Field(alias="normJudgeName")
    ]
    object: str = pydantic.Field()
    """
    Name of the object
    """

    score_constituents: typing_extensions.Annotated[
        typing.Optional[PossibleNormJudgeScoreConstituents],
        FieldMetadata(alias="scoreConstituents"),
        pydantic.Field(alias="scoreConstituents"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
