

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .possible_norm_attorney_score_constituents import PossibleNormAttorneyScoreConstituents


class PossibleNormAttorney(UniversalBaseModel):
    associated_norm_judges_api: typing_extensions.Annotated[
        str, FieldMetadata(alias="associatedNormJudgesAPI"), pydantic.Field(alias="associatedNormJudgesAPI")
    ]
    associated_norm_law_firms_api: typing_extensions.Annotated[
        str, FieldMetadata(alias="associatedNormLawFirmsAPI"), pydantic.Field(alias="associatedNormLawFirmsAPI")
    ]
    associated_norm_parties_api: typing_extensions.Annotated[
        str, FieldMetadata(alias="associatedNormPartiesAPI"), pydantic.Field(alias="associatedNormPartiesAPI")
    ]
    best_match: typing_extensions.Annotated[bool, FieldMetadata(alias="bestMatch"), pydantic.Field(alias="bestMatch")]
    case_count_analytics_by_norm_attorney_api: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="caseCountAnalyticsByNormAttorneyAPI"),
        pydantic.Field(alias="caseCountAnalyticsByNormAttorneyAPI"),
    ]
    case_count_analytics_by_opposing_norm_attorney_api: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="caseCountAnalyticsByOpposingNormAttorneyAPI"),
        pydantic.Field(alias="caseCountAnalyticsByOpposingNormAttorneyAPI"),
    ]
    confidence_score: typing_extensions.Annotated[
        float, FieldMetadata(alias="confidenceScore"), pydantic.Field(alias="confidenceScore")
    ]
    norm_attorney_api: typing_extensions.Annotated[
        str, FieldMetadata(alias="normAttorneyAPI"), pydantic.Field(alias="normAttorneyAPI")
    ]
    norm_attorney_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="normAttorneyId"), pydantic.Field(alias="normAttorneyId")
    ]
    norm_attorney_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="normAttorneyName"), pydantic.Field(alias="normAttorneyName")
    ]
    object: str = pydantic.Field()
    """
    Name of the object
    """

    score_constituents: typing_extensions.Annotated[
        PossibleNormAttorneyScoreConstituents,
        FieldMetadata(alias="scoreConstituents"),
        pydantic.Field(alias="scoreConstituents"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
