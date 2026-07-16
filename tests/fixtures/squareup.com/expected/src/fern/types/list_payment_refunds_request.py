

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListPaymentRefundsRequest(UniversalBaseModel):
    """
    Describes a request to list refunds using
    [ListPaymentRefunds](https://developer.squareup.com/reference/square_2021-08-18/refunds-api/list-payment-refunds).

    The maximum results per page is 100.
    """

    begin_time: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp for the beginning of the requested reporting period, in RFC 3339 format.
    
    Default: The current time minus one year.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    A pagination cursor returned by a previous call to this endpoint.
    Provide this cursor to retrieve the next set of results for the original query.
    
    For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).
    """

    end_time: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp for the end of the requested reporting period, in RFC 3339 format.
    
    Default: The current time.
    """

    limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    The maximum number of results to be returned in a single page.
    
    It is possible to receive fewer results than the specified limit on a given page.
    
    If the supplied value is greater than 100, no more than 100 results are returned.
    
    Default: 100
    """

    location_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Limit results to the location supplied. By default, results are returned
    for all locations associated with the seller.
    """

    sort_order: typing.Optional[str] = pydantic.Field(default=None)
    """
    The order in which results are listed:
    - `ASC` - Oldest to newest.
    - `DESC` - Newest to oldest (default).
    """

    source_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    If provided, only refunds with the given source type are returned.
    - `CARD` - List refunds only for payments where `CARD` was specified as the payment
    source.
    
    Default: If omitted, refunds are returned regardless of the source type.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    If provided, only refunds with the given status are returned.
    For a list of refund status values, see [PaymentRefund](https://developer.squareup.com/reference/square_2021-08-18/objects/PaymentRefund).
    
    Default: If omitted, refunds are returned regardless of their status.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
