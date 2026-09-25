

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .contacts_query_parameters_filter_contact_type import ContactsQueryParametersFilterContactType
from .contacts_query_parameters_sort_field import ContactsQueryParametersSortField
from .contacts_query_parameters_sort_order import ContactsQueryParametersSortOrder


class ContactsQueryParameters(UniversalBaseModel):
    page_size: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="pageSize"), pydantic.Field(alias="pageSize")
    ] = None
    sort_order: typing_extensions.Annotated[
        typing.Optional[ContactsQueryParametersSortOrder],
        FieldMetadata(alias="sortOrder"),
        pydantic.Field(alias="sortOrder"),
    ] = None
    page_cursor: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="pageCursor"), pydantic.Field(alias="pageCursor")
    ] = None
    sort_field: typing_extensions.Annotated[
        typing.Optional[ContactsQueryParametersSortField],
        FieldMetadata(alias="sortField"),
        pydantic.Field(alias="sortField"),
    ] = None
    filter_contact_type: typing_extensions.Annotated[
        typing.Optional[ContactsQueryParametersFilterContactType],
        FieldMetadata(alias="filterContactType"),
        pydantic.Field(alias="filterContactType"),
    ] = None
    filter_customer_id: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="filterCustomerId"), pydantic.Field(alias="filterCustomerId")
    ] = None
    filter_site_id: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="filterSiteId"), pydantic.Field(alias="filterSiteId")
    ] = None
    filter_search_text: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="filterSearchText"),
        pydantic.Field(
            alias="filterSearchText",
            description="Searchable fields:\n- `firstName`\n- `lastName`\n- `email`\n- `phoneNumber`",
        ),
    ] = None
    """
    Searchable fields:
    - `firstName`
    - `lastName`
    - `email`
    - `phoneNumber`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
