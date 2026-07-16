

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .time_range import TimeRange


class SearchOrdersDateTimeFilter(UniversalBaseModel):
    """
    Filter for `Order` objects based on whether their `CREATED_AT`,
    `CLOSED_AT`, or `UPDATED_AT` timestamps fall within a specified time range.
    You can specify the time range and which timestamp to filter for. You can filter
    for only one time range at a time.

    For each time range, the start time and end time are inclusive. If the end time
    is absent, it defaults to the time of the first request for the cursor.

    __Important:__ If you use the `DateTimeFilter` in a `SearchOrders` query,
    you must set the `sort_field` in [OrdersSort](https://developer.squareup.com/reference/square_2021-08-18/objects/SearchOrdersSort)
    to the same field you filter for. For example, if you set the `CLOSED_AT` field
    in `DateTimeFilter`, you must set the `sort_field` in `SearchOrdersSort` to
    `CLOSED_AT`. Otherwise, `SearchOrders` throws an error.
    [Learn more about filtering orders by time range.](https://developer.squareup.com/docs/orders-api/manage-orders#important-note-on-filtering-orders-by-time-range)
    """

    closed_at: typing.Optional[TimeRange] = None
    created_at: typing.Optional[TimeRange] = None
    updated_at: typing.Optional[TimeRange] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
