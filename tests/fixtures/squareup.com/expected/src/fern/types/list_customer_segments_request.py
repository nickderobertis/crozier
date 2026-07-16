

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListCustomerSegmentsRequest(UniversalBaseModel):
    """
    Defines the valid parameters for requests to the `ListCustomerSegments` endpoint.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    A pagination cursor returned by previous calls to `ListCustomerSegments`.
    This cursor is used to retrieve the next set of query results.
    
    For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    """

    limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    The maximum number of results to return in a single page. This limit is advisory. The response might contain more or fewer results. 
    The limit is ignored if it is less than 1 or greater than 50. The default value is 50.
    
    For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
