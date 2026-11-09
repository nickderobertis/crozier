

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .possible_norm_law_firm_score_constituents import PossibleNormLawFirmScoreConstituents
from .possible_norm_law_firm_source_details import PossibleNormLawFirmSourceDetails


class PossibleNormLawFirm(UniversalBaseModel):
    associated_norm_attorney_api: typing_extensions.Annotated[
        str, FieldMetadata(alias="associatedNormAttorneyAPI"), pydantic.Field(alias="associatedNormAttorneyAPI")
    ]
    associated_norm_judge_api: typing_extensions.Annotated[
        str, FieldMetadata(alias="associatedNormJudgeAPI"), pydantic.Field(alias="associatedNormJudgeAPI")
    ]
    associated_norm_parties_api: typing_extensions.Annotated[
        str, FieldMetadata(alias="associatedNormPartiesAPI"), pydantic.Field(alias="associatedNormPartiesAPI")
    ]
    best_match: typing_extensions.Annotated[bool, FieldMetadata(alias="bestMatch"), pydantic.Field(alias="bestMatch")]
    case_count_analytics_by_norm_law_firm_api: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="caseCountAnalyticsByNormLawFirmAPI"),
        pydantic.Field(alias="caseCountAnalyticsByNormLawFirmAPI"),
    ]
    case_count_analytics_by_opposing_norm_law_firm_api: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="caseCountAnalyticsByOpposingNormLawFirmAPI"),
        pydantic.Field(alias="caseCountAnalyticsByOpposingNormLawFirmAPI"),
    ]
    confidence_score: typing_extensions.Annotated[
        float, FieldMetadata(alias="confidenceScore"), pydantic.Field(alias="confidenceScore")
    ]
    norm_law_firm_api: typing_extensions.Annotated[
        str, FieldMetadata(alias="normLawFirmAPI"), pydantic.Field(alias="normLawFirmAPI")
    ]
    norm_law_firm_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="normLawFirmId"), pydantic.Field(alias="normLawFirmId")
    ]
    norm_law_firm_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="normLawFirmName"), pydantic.Field(alias="normLawFirmName")
    ]
    object: str = pydantic.Field()
    """
    Name of the object
    """

    score_constituents: typing_extensions.Annotated[
        PossibleNormLawFirmScoreConstituents,
        FieldMetadata(alias="scoreConstituents"),
        pydantic.Field(alias="scoreConstituents"),
    ]
    source_details: typing_extensions.Annotated[
        PossibleNormLawFirmSourceDetails, FieldMetadata(alias="sourceDetails"), pydantic.Field(alias="sourceDetails")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
