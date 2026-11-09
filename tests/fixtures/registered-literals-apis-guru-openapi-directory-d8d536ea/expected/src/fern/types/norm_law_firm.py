

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .case_analytics_api import CaseAnalyticsApi
from .law_firm_analytics_api import LawFirmAnalyticsApi
from .norm_organization import NormOrganization


class NormLawFirm(UniversalBaseModel):
    """
    Schema for Norm Law Firm containing Organization sub-field.
    """

    case_analytics_api: typing_extensions.Annotated[
        CaseAnalyticsApi, FieldMetadata(alias="caseAnalyticsAPI"), pydantic.Field(alias="caseAnalyticsAPI")
    ]
    case_search_api: typing_extensions.Annotated[
        str, FieldMetadata(alias="caseSearchAPI"), pydantic.Field(alias="caseSearchAPI")
    ]
    law_firm_analytics_api: typing_extensions.Annotated[
        LawFirmAnalyticsApi, FieldMetadata(alias="lawFirmAnalyticsAPI"), pydantic.Field(alias="lawFirmAnalyticsAPI")
    ]
    name: str
    norm_law_firm_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="normLawFirmId"), pydantic.Field(alias="normLawFirmId")
    ]
    norm_organization_data: typing_extensions.Annotated[
        NormOrganization, FieldMetadata(alias="normOrganizationData"), pydantic.Field(alias="normOrganizationData")
    ]
    object: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
