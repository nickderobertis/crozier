

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .case_analytics_api import CaseAnalyticsApi
from .judge_analytics_api import JudgeAnalyticsApi
from .norm_judge_public_data import NormJudgePublicData


class NormJudge(UniversalBaseModel):
    """
    Norm Judge
    """

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
    judge_analytics_api: typing_extensions.Annotated[
        JudgeAnalyticsApi, FieldMetadata(alias="judgeAnalyticsAPI"), pydantic.Field(alias="judgeAnalyticsAPI")
    ]
    judicial_data_array: typing_extensions.Annotated[
        typing.List[NormJudgePublicData],
        FieldMetadata(alias="judicialDataArray"),
        pydantic.Field(alias="judicialDataArray"),
    ]
    last_name: typing_extensions.Annotated[str, FieldMetadata(alias="lastName"), pydantic.Field(alias="lastName")]
    middle_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="middleName"), pydantic.Field(alias="middleName")
    ] = None
    name: str
    norm_judge_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="normJudgeId"), pydantic.Field(alias="normJudgeId")
    ]
    object: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
