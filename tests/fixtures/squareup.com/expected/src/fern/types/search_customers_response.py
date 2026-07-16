

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .customer import Customer
from .error import Error


class SearchCustomersResponse(UniversalBaseModel):
    """
    Defines the fields that are included in the response body of
    a request to the `SearchCustomers` endpoint.

    Either `errors` or `customers` is present in a given response (never both).
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    A pagination cursor that can be used during subsequent calls
    to `SearchCustomers` to retrieve the next set of results associated
    with the original query. Pagination cursors are only present when
    a request succeeds and additional results are available.
    
    For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    """

    customers: typing.Optional[typing.List[Customer]] = pydantic.Field(default=None)
    """
    An array of `Customer` objects that match a query.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
