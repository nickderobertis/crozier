

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PartyAnalyticsApi(UniversalBaseModel):
    associated_norm_attorneys_api: typing_extensions.Annotated[
        str, FieldMetadata(alias="associatedNormAttorneysAPI"), pydantic.Field(alias="associatedNormAttorneysAPI")
    ]
    associated_norm_judges_api: typing_extensions.Annotated[
        str, FieldMetadata(alias="associatedNormJudgesAPI"), pydantic.Field(alias="associatedNormJudgesAPI")
    ]
    associated_norm_law_firms_api: typing_extensions.Annotated[
        str, FieldMetadata(alias="associatedNormLawFirmsAPI"), pydantic.Field(alias="associatedNormLawFirmsAPI")
    ]
    case_count_analytics_by_opposing_norm_attorney_api: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="caseCountAnalyticsByOpposingNormAttorneyAPI"),
        pydantic.Field(alias="caseCountAnalyticsByOpposingNormAttorneyAPI"),
    ] = None
    case_count_analytics_by_opposing_norm_law_firm_api: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="caseCountAnalyticsByOpposingNormLawFirmAPI"),
        pydantic.Field(alias="caseCountAnalyticsByOpposingNormLawFirmAPI"),
    ] = None
    case_count_analytics_by_opposing_norm_party_api: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="caseCountAnalyticsByOpposingNormPartyAPI"),
        pydantic.Field(alias="caseCountAnalyticsByOpposingNormPartyAPI"),
    ]
    norm_party_api: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="normPartyAPI"),
        pydantic.Field(alias="normPartyAPI", description="Link to Details for the Party."),
    ]
    """
    Link to Details for the Party.
    """

    object: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
