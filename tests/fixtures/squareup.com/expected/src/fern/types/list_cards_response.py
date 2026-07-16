

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .card import Card
from .error import Error


class ListCardsResponse(UniversalBaseModel):
    """
    Defines the fields that are included in the response body of
    a request to the [ListCards](#endpoint-cards-listcards) endpoint.

    Note: if there are errors processing the request, the card field will not be
    present.
    """

    cards: typing.Optional[typing.List[Card]] = pydantic.Field(default=None)
    """
    The requested list of `Card`s.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    The pagination cursor to be used in a subsequent request. If empty,
    this is the final response.
    
    See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Information on errors encountered during the request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
