

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .case_count_analytics_by_case_filed_date_grouped_by import CaseCountAnalyticsByCaseFiledDateGroupedBy
from .case_count_analytics_by_case_filed_date_month_string import CaseCountAnalyticsByCaseFiledDateMonthString
from .case_count_analytics_by_case_filed_date_quarter import CaseCountAnalyticsByCaseFiledDateQuarter


class CaseCountAnalyticsByCaseFiledDate(UniversalBaseModel):
    case_count: typing_extensions.Annotated[int, FieldMetadata(alias="caseCount"), pydantic.Field(alias="caseCount")]
    case_search_api: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="caseSearchAPI"),
        pydantic.Field(alias="caseSearchAPI", description="Link to cases for this criteria."),
    ]
    """
    Link to cases for this criteria.
    """

    grouped_by: typing_extensions.Annotated[
        CaseCountAnalyticsByCaseFiledDateGroupedBy, FieldMetadata(alias="groupedBy"), pydantic.Field(alias="groupedBy")
    ]
    month_int: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="monthInt"), pydantic.Field(alias="monthInt")
    ] = None
    month_string: typing_extensions.Annotated[
        typing.Optional[CaseCountAnalyticsByCaseFiledDateMonthString],
        FieldMetadata(alias="monthString"),
        pydantic.Field(alias="monthString"),
    ] = None
    object: str
    quarter: typing.Optional[CaseCountAnalyticsByCaseFiledDateQuarter] = None
    week_of_month: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="weekOfMonth"), pydantic.Field(alias="weekOfMonth")
    ] = None
    week_of_year: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="weekOfYear"), pydantic.Field(alias="weekOfYear")
    ] = None
    year: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
