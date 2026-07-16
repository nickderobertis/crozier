

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListCustomerGroupsRequest(UniversalBaseModel):
    """
    Defines the query parameters that can be included in a request to the
    [ListCustomerGroups](https://developer.squareup.com/reference/square_2021-08-18/customer-groups-api/list-customer-groups) endpoint.
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
