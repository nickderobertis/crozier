

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .search_orders_customer_filter import SearchOrdersCustomerFilter
from .search_orders_date_time_filter import SearchOrdersDateTimeFilter
from .search_orders_fulfillment_filter import SearchOrdersFulfillmentFilter
from .search_orders_source_filter import SearchOrdersSourceFilter
from .search_orders_state_filter import SearchOrdersStateFilter


class SearchOrdersFilter(UniversalBaseModel):
    """
    Filtering criteria to use for a `SearchOrders` request. Multiple filters
    are ANDed together.
    """

    customer_filter: typing.Optional[SearchOrdersCustomerFilter] = None
    date_time_filter: typing.Optional[SearchOrdersDateTimeFilter] = None
    fulfillment_filter: typing.Optional[SearchOrdersFulfillmentFilter] = None
    source_filter: typing.Optional[SearchOrdersSourceFilter] = None
    state_filter: typing.Optional[SearchOrdersStateFilter] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
