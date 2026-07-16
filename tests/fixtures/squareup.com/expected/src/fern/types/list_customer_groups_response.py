

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .customer_group import CustomerGroup
from .error import Error


class ListCustomerGroupsResponse(UniversalBaseModel):
    """
    Defines the fields that are included in the response body of
    a request to the [ListCustomerGroups](https://developer.squareup.com/reference/square_2021-08-18/customer-groups-api/list-customer-groups) endpoint.

    Either `errors` or `groups` is present in a given response (never both).
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    A pagination cursor to retrieve the next set of results for your
    original query to the endpoint. This value is present only if the request
    succeeded and additional results are available.
    
    For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    groups: typing.Optional[typing.List[CustomerGroup]] = pydantic.Field(default=None)
    """
    A list of customer groups belonging to the current seller.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
