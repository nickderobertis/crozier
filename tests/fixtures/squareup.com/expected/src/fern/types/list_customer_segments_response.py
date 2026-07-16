

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .customer_segment import CustomerSegment
from .error import Error


class ListCustomerSegmentsResponse(UniversalBaseModel):
    """
    Defines the fields that are included in the response body for requests to the `ListCustomerSegments` endpoint.

    Either `errors` or `segments` is present in a given response (never both).
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    A pagination cursor to be used in subsequent calls to `ListCustomerSegments`
    to retrieve the next set of query results. The cursor is only present if the request succeeded and
    additional results are available.
    
    For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    segments: typing.Optional[typing.List[CustomerSegment]] = pydantic.Field(default=None)
    """
    The list of customer segments belonging to the associated Square account.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
