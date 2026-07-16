

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error import Error
from .loyalty_event import LoyaltyEvent


class SearchLoyaltyEventsResponse(UniversalBaseModel):
    """
    A response that contains loyalty events that satisfy the search
    criteria, in order by the `created_at` date.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    The pagination cursor to be used in a subsequent 
    request. If empty, this is the final response. 
    For more information, 
    see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    events: typing.Optional[typing.List[LoyaltyEvent]] = pydantic.Field(default=None)
    """
    The loyalty events that satisfy the search criteria.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
