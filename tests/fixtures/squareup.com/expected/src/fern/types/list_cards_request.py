

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListCardsRequest(UniversalBaseModel):
    """
    Retrieves details for a specific Card. Accessible via
    HTTP requests at GET https://connect.squareup.com/v2/cards
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    A pagination cursor returned by a previous call to this endpoint.
    Provide this to retrieve the next set of results for your original query.
    
    See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information.
    """

    customer_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Limit results to cards associated with the customer supplied.
    By default, all cards owned by the merchant are returned.
    """

    include_disabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Includes disabled cards.
    By default, all enabled cards owned by the merchant are returned.
    """

    reference_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Limit results to cards associated with the reference_id supplied.
    """

    sort_order: typing.Optional[str] = pydantic.Field(default=None)
    """
    Sorts the returned list by when the card was created with the specified order.
    This field defaults to ASC.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
