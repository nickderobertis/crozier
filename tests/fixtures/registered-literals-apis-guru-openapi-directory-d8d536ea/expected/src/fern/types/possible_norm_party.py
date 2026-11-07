

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .possible_norm_party_score_constituents import PossibleNormPartyScoreConstituents


class PossibleNormParty(UniversalBaseModel):
    associated_norm_attorneys_api: typing_extensions.Annotated[
        str, FieldMetadata(alias="associatedNormAttorneysAPI"), pydantic.Field(alias="associatedNormAttorneysAPI")
    ]
    associated_norm_judges_api: typing_extensions.Annotated[
        str, FieldMetadata(alias="associatedNormJudgesAPI"), pydantic.Field(alias="associatedNormJudgesAPI")
    ]
    associated_norm_law_firms_api: typing_extensions.Annotated[
        str, FieldMetadata(alias="associatedNormLawFirmsAPI"), pydantic.Field(alias="associatedNormLawFirmsAPI")
    ]
    best_match: typing_extensions.Annotated[bool, FieldMetadata(alias="bestMatch"), pydantic.Field(alias="bestMatch")]
    case_count_analytics_by_norm_party_api: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="caseCountAnalyticsByNormPartyAPI"),
        pydantic.Field(alias="caseCountAnalyticsByNormPartyAPI"),
    ]
    case_count_analytics_by_opposing_norm_party_api: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="caseCountAnalyticsByOpposingNormPartyAPI"),
        pydantic.Field(alias="caseCountAnalyticsByOpposingNormPartyAPI"),
    ]
    confidence_score: typing_extensions.Annotated[
        float, FieldMetadata(alias="confidenceScore"), pydantic.Field(alias="confidenceScore")
    ]
    norm_party_api: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="normPartyAPI"),
        pydantic.Field(alias="normPartyAPI", description="Link to Details For the Party."),
    ]
    """
    Link to Details For the Party.
    """

    norm_party_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="normPartyId"), pydantic.Field(alias="normPartyId")
    ]
    norm_party_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="normPartyName"), pydantic.Field(alias="normPartyName")
    ]
    object: str = pydantic.Field()
    """
    Name of the object
    """

    score_constituents: typing_extensions.Annotated[
        PossibleNormPartyScoreConstituents,
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
