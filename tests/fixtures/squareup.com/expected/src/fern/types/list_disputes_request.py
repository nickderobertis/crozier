

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListDisputesRequest(UniversalBaseModel):
    """
    Defines the request parameters for the `ListDisputes` endpoint.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    A pagination cursor returned by a previous call to this endpoint.
    Provide this cursor to retrieve the next set of results for the original query.
    For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).
    """

    location_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the location for which to return a list of disputes. If not specified, the endpoint returns
    all open disputes (the dispute status is not `INQUIRY_CLOSED`, `WON`, or `LOST`) associated with all locations.
    """

    states: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The dispute states to filter the result.
    If not specified, the endpoint returns all open disputes (the dispute status is not `INQUIRY_CLOSED`, `WON`,
    or `LOST`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
