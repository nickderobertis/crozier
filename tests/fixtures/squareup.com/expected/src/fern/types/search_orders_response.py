

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error import Error
from .order import Order
from .order_entry import OrderEntry


class SearchOrdersResponse(UniversalBaseModel):
    """
    Either the `order_entries` or `orders` field is set, depending on whether
    `return_entries` is set on the [SearchOrdersRequest](https://developer.squareup.com/reference/square_2021-08-18/orders-api/search-orders).
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    The pagination cursor to be used in a subsequent request. If unset,
    this is the final response.
    For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    [Errors](https://developer.squareup.com/reference/square_2021-08-18/objects/Error) encountered during the search.
    """

    order_entries: typing.Optional[typing.List[OrderEntry]] = pydantic.Field(default=None)
    """
    A list of [OrderEntries](https://developer.squareup.com/reference/square_2021-08-18/objects/OrderEntry) that fit the query
    conditions. The list is populated only if `return_entries` is set to `true` in the request.
    """

    orders: typing.Optional[typing.List[Order]] = pydantic.Field(default=None)
    """
    A list of
    [Order](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) objects that match the query conditions. The list is populated only if
    `return_entries` is set to `false` in the request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
