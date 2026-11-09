

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CaseAnalyticsApi(UniversalBaseModel):
    """
    Provides Court Data per State Jurisdiction for an entity.
    """

    case_count_analytics_by_area_of_law_api: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="caseCountAnalyticsByAreaOfLawAPI"),
        pydantic.Field(alias="caseCountAnalyticsByAreaOfLawAPI"),
    ]
    case_count_analytics_by_case_class_api: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="caseCountAnalyticsByCaseClassAPI"),
        pydantic.Field(alias="caseCountAnalyticsByCaseClassAPI"),
    ]
    case_count_analytics_by_case_type_api: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="caseCountAnalyticsByCaseTypeAPI"),
        pydantic.Field(alias="caseCountAnalyticsByCaseTypeAPI"),
    ]
    case_count_analytics_by_case_type_group_api: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="caseCountAnalyticsByCaseTypeGroupAPI"),
        pydantic.Field(alias="caseCountAnalyticsByCaseTypeGroupAPI"),
    ]
    case_count_analytics_by_court_api: typing_extensions.Annotated[
        str, FieldMetadata(alias="caseCountAnalyticsByCourtAPI"), pydantic.Field(alias="caseCountAnalyticsByCourtAPI")
    ]
    case_count_analytics_by_court_location_api: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="caseCountAnalyticsByCourtLocationAPI"),
        pydantic.Field(alias="caseCountAnalyticsByCourtLocationAPI"),
    ]
    case_count_analytics_by_court_system_api: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="caseCountAnalyticsByCourtSystemAPI"),
        pydantic.Field(alias="caseCountAnalyticsByCourtSystemAPI"),
    ]
    case_count_analytics_by_court_type_api: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="caseCountAnalyticsByCourtTypeAPI"),
        pydantic.Field(alias="caseCountAnalyticsByCourtTypeAPI"),
    ]
    case_count_analytics_by_jurisdiction_geo_api: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="caseCountAnalyticsByJurisdictionGeoAPI"),
        pydantic.Field(alias="caseCountAnalyticsByJurisdictionGeoAPI"),
    ]
    case_count_analytics_by_party_role_api: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="caseCountAnalyticsByPartyRoleAPI"),
        pydantic.Field(alias="caseCountAnalyticsByPartyRoleAPI"),
    ] = None
    case_count_analytics_by_party_role_group_api: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="caseCountAnalyticsByPartyRoleGroupAPI"),
        pydantic.Field(alias="caseCountAnalyticsByPartyRoleGroupAPI"),
    ] = None
    object: str
    total_cases: typing_extensions.Annotated[int, FieldMetadata(alias="totalCases"), pydantic.Field(alias="totalCases")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
