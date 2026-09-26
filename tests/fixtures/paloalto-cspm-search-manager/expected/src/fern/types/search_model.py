

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .search_model_cloud_type import SearchModelCloudType
from .search_model_search_type import SearchModelSearchType
from .search_model_time_range import SearchModelTimeRange
from .ui_filter_model import UiFilterModel


class SearchModel(UniversalBaseModel):
    alert_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="alertId"), pydantic.Field(alias="alertId", description="Alert ID")
    ] = None
    """
    Alert ID
    """

    async_: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="async"),
        pydantic.Field(alias="async", description="true = Is Async"),
    ] = None
    """
    true = Is Async
    """

    async_result_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="asyncResultUrl"),
        pydantic.Field(alias="asyncResultUrl", description="Async Result Url"),
    ] = None
    """
    Async Result Url
    """

    cloud_type: typing_extensions.Annotated[
        typing.Optional[SearchModelCloudType],
        FieldMetadata(alias="cloudType"),
        pydantic.Field(alias="cloudType", description="Cloud Type"),
    ] = None
    """
    Cloud Type
    """

    cursor: typing.Optional[int] = pydantic.Field(default=None)
    """
    Cursor
    """

    default: typing.Optional[bool] = None
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Search Description
    """

    filters: typing.Optional[typing.List[UiFilterModel]] = pydantic.Field(default=None)
    """
    View Order
    """

    group_by: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="groupBy"),
        pydantic.Field(alias="groupBy", description="Group By"),
    ] = None
    """
    Group By
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Search ID
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Search Name
    """

    query: str = pydantic.Field()
    """
    RQL Query
    """

    read_only: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="readOnly"),
        pydantic.Field(alias="readOnly", description="Read Only"),
    ] = None
    """
    Read Only
    """

    saved: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Search Exists
    """

    search_type: typing_extensions.Annotated[
        typing.Optional[SearchModelSearchType],
        FieldMetadata(alias="searchType"),
        pydantic.Field(alias="searchType", description="Search Type"),
    ] = None
    """
    Search Type
    """

    time_granularity: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="timeGranularity"),
        pydantic.Field(alias="timeGranularity", description="Time Granularity"),
    ] = None
    """
    Time Granularity
    """

    time_range: typing_extensions.Annotated[
        SearchModelTimeRange,
        FieldMetadata(alias="timeRange"),
        pydantic.Field(alias="timeRange", description="Time Range"),
    ]
    """
    Time Range
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
