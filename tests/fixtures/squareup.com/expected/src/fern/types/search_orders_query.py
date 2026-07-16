

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .search_orders_filter import SearchOrdersFilter
from .search_orders_sort import SearchOrdersSort


class SearchOrdersQuery(UniversalBaseModel):
    """
    Contains query criteria for the search.
    """

    filter: typing.Optional[SearchOrdersFilter] = None
    sort: typing.Optional[SearchOrdersSort] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
