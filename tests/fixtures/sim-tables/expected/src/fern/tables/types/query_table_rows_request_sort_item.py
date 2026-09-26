

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .query_table_rows_request_sort_item_direction import QueryTableRowsRequestSortItemDirection


class QueryTableRowsRequestSortItem(UniversalBaseModel):
    field: str = pydantic.Field()
    """
    Column name to sort by.
    """

    direction: QueryTableRowsRequestSortItemDirection = pydantic.Field()
    """
    Sort direction for this column.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
