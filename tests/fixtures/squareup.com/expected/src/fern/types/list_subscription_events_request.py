

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListSubscriptionEventsRequest(UniversalBaseModel):
    """
    Defines parameters in a
    [ListSubscriptionEvents](https://developer.squareup.com/reference/square_2021-08-18/subscriptions-api/list-subscription-events)
    endpoint request.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    A pagination cursor returned by a previous call to this endpoint.
    Provide this to retrieve the next set of results for the original query.
    
    For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    """

    limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    The upper limit on the number of subscription events to return
    in the response.
    
    Default: `200`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
