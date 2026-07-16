

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListTransactionsRequest(UniversalBaseModel):
    """
    Defines the query parameters that can be included in
    a request to the [ListTransactions](https://developer.squareup.com/reference/square_2021-08-18/transactions-api/list-transactions) endpoint.

    Deprecated - recommend using [SearchOrders](https://developer.squareup.com/reference/square_2021-08-18/orders-api/search-orders)
    """

    begin_time: typing.Optional[str] = pydantic.Field(default=None)
    """
    The beginning of the requested reporting period, in RFC 3339 format.
    
    See [Date ranges](https://developer.squareup.com/docs/build-basics/working-with-dates) for details on date inclusivity/exclusivity.
    
    Default value: The current time minus one year.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    A pagination cursor returned by a previous call to this endpoint.
    Provide this to retrieve the next set of results for your original query.
    
    See [Paginating results](https://developer.squareup.com/docs/working-with-apis/pagination) for more information.
    """

    end_time: typing.Optional[str] = pydantic.Field(default=None)
    """
    The end of the requested reporting period, in RFC 3339 format.
    
    See [Date ranges](https://developer.squareup.com/docs/build-basics/working-with-dates) for details on date inclusivity/exclusivity.
    
    Default value: The current time.
    """

    sort_order: typing.Optional[str] = pydantic.Field(default=None)
    """
    The order in which results are listed in the response (`ASC` for
    oldest first, `DESC` for newest first).
    
    Default value: `DESC`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
