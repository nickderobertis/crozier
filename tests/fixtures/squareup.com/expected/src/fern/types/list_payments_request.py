

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ListPaymentsRequest(UniversalBaseModel):
    """
    Describes a request to list payments using
    [ListPayments](https://developer.squareup.com/reference/square_2021-08-18/payments-api/list-payments).

    The maximum results per page is 100.
    """

    begin_time: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp for the beginning of the reporting period, in RFC 3339 format.
    Inclusive. Default: The current time minus one year.
    """

    card_brand: typing.Optional[str] = pydantic.Field(default=None)
    """
    The brand of the payment card (for example, VISA).
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    A pagination cursor returned by a previous call to this endpoint.
    Provide this cursor to retrieve the next set of results for the original query.
    
    For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).
    """

    end_time: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp for the end of the reporting period, in RFC 3339 format.
    
    Default: The current time.
    """

    last4: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="last_4")] = pydantic.Field(
        default=None
    )
    """
    The last four digits of a payment card.
    """

    limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    The maximum number of results to be returned in a single page.
    It is possible to receive fewer results than the specified limit on a given page.
    
    The default value of 100 is also the maximum allowed value. If the provided value is 
    greater than 100, it is ignored and the default value is used instead.
    
    Default: `100`
    """

    location_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Limit results to the location supplied. By default, results are returned
    for the default (main) location associated with the seller.
    """

    sort_order: typing.Optional[str] = pydantic.Field(default=None)
    """
    The order in which results are listed:
    - `ASC` - Oldest to newest.
    - `DESC` - Newest to oldest (default).
    """

    total: typing.Optional[int] = pydantic.Field(default=None)
    """
    The exact amount in the `total_money` for a payment.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
