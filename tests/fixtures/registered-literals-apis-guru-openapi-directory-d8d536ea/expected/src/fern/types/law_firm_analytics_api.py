

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LawFirmAnalyticsApi(UniversalBaseModel):
    associated_norm_attorney_api: typing_extensions.Annotated[
        str, FieldMetadata(alias="associatedNormAttorneyAPI"), pydantic.Field(alias="associatedNormAttorneyAPI")
    ]
    associated_norm_judge_api: typing_extensions.Annotated[
        str, FieldMetadata(alias="associatedNormJudgeAPI"), pydantic.Field(alias="associatedNormJudgeAPI")
    ]
    associated_norm_parties_api: typing_extensions.Annotated[
        str, FieldMetadata(alias="associatedNormPartiesAPI"), pydantic.Field(alias="associatedNormPartiesAPI")
    ]
    case_count_analytics_by_opposing_norm_attorney_api: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="caseCountAnalyticsByOpposingNormAttorneyAPI"),
        pydantic.Field(alias="caseCountAnalyticsByOpposingNormAttorneyAPI"),
    ] = None
    case_count_analytics_by_opposing_norm_law_firm_api: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="caseCountAnalyticsByOpposingNormLawFirmAPI"),
        pydantic.Field(alias="caseCountAnalyticsByOpposingNormLawFirmAPI"),
    ]
    case_count_analytics_by_opposing_norm_party_api: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="caseCountAnalyticsByOpposingNormPartyAPI"),
        pydantic.Field(alias="caseCountAnalyticsByOpposingNormPartyAPI"),
    ] = None
    norm_law_firm_api: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="normLawFirmAPI"),
        pydantic.Field(alias="normLawFirmAPI", description="Link to Details for the Law Firm."),
    ]
    """
    Link to Details for the Law Firm.
    """

    object: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
