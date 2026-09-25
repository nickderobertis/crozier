

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .stock_on_hand_query_parameters_sort_field import StockOnHandQueryParametersSortField
from .stock_on_hand_query_parameters_sort_order import StockOnHandQueryParametersSortOrder


class StockOnHandQueryParameters(UniversalBaseModel):
    page_size: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="pageSize"), pydantic.Field(alias="pageSize")
    ] = None
    sort_order: typing_extensions.Annotated[
        typing.Optional[StockOnHandQueryParametersSortOrder],
        FieldMetadata(alias="sortOrder"),
        pydantic.Field(alias="sortOrder"),
    ] = None
    page_cursor: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="pageCursor"), pydantic.Field(alias="pageCursor")
    ] = None
    sort_field: typing_extensions.Annotated[
        typing.Optional[StockOnHandQueryParametersSortField],
        FieldMetadata(alias="sortField"),
        pydantic.Field(alias="sortField"),
    ] = None
    filter_search_text: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="filterSearchText"),
        pydantic.Field(alias="filterSearchText", description="Searchable fields:\n- `itemDescription`"),
    ] = None
    """
    Searchable fields:
    - `itemDescription`
    """

    last_modified: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="lastModified"), pydantic.Field(alias="lastModified")
    ] = None
    date_entered: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="dateEntered"), pydantic.Field(alias="dateEntered")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
