

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListInvoicesRequest(UniversalBaseModel):
    """
    Describes a `ListInvoice` request.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    A pagination cursor returned by a previous call to this endpoint. 
    Provide this cursor to retrieve the next set of results for your original query.
    
    For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    """

    limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    The maximum number of invoices to return (200 is the maximum `limit`). 
    If not provided, the server uses a default limit of 100 invoices.
    """

    location_id: str = pydantic.Field()
    """
    The ID of the location for which to list invoices.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
