

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListCustomersRequest(UniversalBaseModel):
    """
    Defines the query parameters that can be included in a request to the
    `ListCustomers` endpoint.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    A pagination cursor returned by a previous call to this endpoint.
    Provide this cursor to retrieve the next set of results for your original query.
    
    For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    """

    limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    The maximum number of results to return in a single page. This limit is advisory. The response might contain more or fewer results. 
    The limit is ignored if it is less than 1 or greater than 100. The default value is 100.
    
    For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    """

    sort_field: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicates how customers should be sorted.
    
    The default value is `DEFAULT`.
    """

    sort_order: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicates whether customers should be sorted in ascending (`ASC`) or
    descending (`DESC`) order.
    
    The default value is `ASC`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
