

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .jobs_query_parameters_filter_job_status import JobsQueryParametersFilterJobStatus
from .jobs_query_parameters_filter_job_type import JobsQueryParametersFilterJobType
from .jobs_query_parameters_sort_field import JobsQueryParametersSortField
from .jobs_query_parameters_sort_order import JobsQueryParametersSortOrder


class JobsQueryParameters(UniversalBaseModel):
    page_size: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="pageSize"), pydantic.Field(alias="pageSize")
    ] = None
    sort_order: typing_extensions.Annotated[
        typing.Optional[JobsQueryParametersSortOrder],
        FieldMetadata(alias="sortOrder"),
        pydantic.Field(alias="sortOrder"),
    ] = None
    page_cursor: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="pageCursor"), pydantic.Field(alias="pageCursor")
    ] = None
    filter_job_no: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="filterJobNo"), pydantic.Field(alias="filterJobNo")
    ] = None
    filter_job_status: typing_extensions.Annotated[
        typing.Optional[JobsQueryParametersFilterJobStatus],
        FieldMetadata(alias="filterJobStatus"),
        pydantic.Field(alias="filterJobStatus"),
    ] = None
    filter_job_type: typing_extensions.Annotated[
        typing.Optional[JobsQueryParametersFilterJobType],
        FieldMetadata(alias="filterJobType"),
        pydantic.Field(alias="filterJobType"),
    ] = None
    filter_customer_id: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="filterCustomerId"), pydantic.Field(alias="filterCustomerId")
    ] = None
    filter_site_id: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="filterSiteId"), pydantic.Field(alias="filterSiteId")
    ] = None
    sort_field: typing_extensions.Annotated[
        typing.Optional[JobsQueryParametersSortField],
        FieldMetadata(alias="sortField"),
        pydantic.Field(alias="sortField"),
    ] = None
    filter_show_on_hold: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="filterShowOnHold"), pydantic.Field(alias="filterShowOnHold")
    ] = None
    filter_show_archived: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="filterShowArchived"), pydantic.Field(alias="filterShowArchived")
    ] = None
    filter_search_text: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="filterSearchText"),
        pydantic.Field(
            alias="filterSearchText",
            description="Searchable fields:\n- `description`\n- `longDescription`\n- `jobNo`\n- `customer.customerFullName`\n- `siteAddress.name`\n- `siteAddress.firstName`\n- `siteAddress.lastName`\n- `mainContact.firstName`\n- `mainContact.lastName`",
        ),
    ] = None
    """
    Searchable fields:
    - `description`
    - `longDescription`
    - `jobNo`
    - `customer.customerFullName`
    - `siteAddress.name`
    - `siteAddress.firstName`
    - `siteAddress.lastName`
    - `mainContact.firstName`
    - `mainContact.lastName`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
