

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RetrieveInventoryChangesRequest(UniversalBaseModel):
    """ """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    A pagination cursor returned by a previous call to this endpoint.
    Provide this to retrieve the next set of results for the original query.
    
    See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.
    """

    location_ids: typing.Optional[str] = pydantic.Field(default=None)
    """
    The [Location](https://developer.squareup.com/reference/square_2021-08-18/objects/Location) IDs to look up as a comma-separated
    list. An empty list queries all locations.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
