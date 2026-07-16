

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error import Error
from .subscription import Subscription


class SearchSubscriptionsResponse(UniversalBaseModel):
    """
    Defines the fields that are included in the response from the
    [SearchSubscriptions](https://developer.squareup.com/reference/square_2021-08-18/subscriptions-api/search-subscriptions) endpoint.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    When a response is truncated, it includes a cursor that you can
    use in a subsequent request to fetch the next set of subscriptions.
    If empty, this is the final response.
    
    For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Information about errors encountered during the request.
    """

    subscriptions: typing.Optional[typing.List[Subscription]] = pydantic.Field(default=None)
    """
    The search result.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
