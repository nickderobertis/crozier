

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .attorney_analytics_api import AttorneyAnalyticsApi
from .bar_record import BarRecord
from .case_analytics_api import CaseAnalyticsApi
from .similar_norm_attorney import SimilarNormAttorney


class NormAttorney(UniversalBaseModel):
    """
    Norm Attorney
    """

    attorney_analytics_api: typing_extensions.Annotated[
        AttorneyAnalyticsApi, FieldMetadata(alias="attorneyAnalyticsAPI"), pydantic.Field(alias="attorneyAnalyticsAPI")
    ]
    bar_record_array: typing_extensions.Annotated[
        typing.List[BarRecord], FieldMetadata(alias="barRecordArray"), pydantic.Field(alias="barRecordArray")
    ]
    case_analytics_api: typing_extensions.Annotated[
        CaseAnalyticsApi, FieldMetadata(alias="caseAnalyticsAPI"), pydantic.Field(alias="caseAnalyticsAPI")
    ]
    case_search_api: typing_extensions.Annotated[
        str, FieldMetadata(alias="caseSearchAPI"), pydantic.Field(alias="caseSearchAPI")
    ]
    first_name: typing_extensions.Annotated[str, FieldMetadata(alias="firstName"), pydantic.Field(alias="firstName")]
    has_associated_public_data: typing_extensions.Annotated[
        bool, FieldMetadata(alias="hasAssociatedPublicData"), pydantic.Field(alias="hasAssociatedPublicData")
    ]
    last_name: typing_extensions.Annotated[str, FieldMetadata(alias="lastName"), pydantic.Field(alias="lastName")]
    middle_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="middleName"), pydantic.Field(alias="middleName")
    ] = None
    name: str
    norm_attorney_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="normAttorneyId"), pydantic.Field(alias="normAttorneyId")
    ]
    object: str
    similar_norm_attorney_array: typing_extensions.Annotated[
        typing.List[SimilarNormAttorney],
        FieldMetadata(alias="similarNormAttorneyArray"),
        pydantic.Field(alias="similarNormAttorneyArray"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
