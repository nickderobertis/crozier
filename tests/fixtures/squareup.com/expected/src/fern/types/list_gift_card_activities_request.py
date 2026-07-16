

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListGiftCardActivitiesRequest(UniversalBaseModel):
    """
    Returns a list of gift card activities. You can optionally specify a filter to retrieve a
    subset of activites.
    """

    begin_time: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp for the beginning of the reporting period, in RFC 3339 format.
    Inclusive. Default: The current time minus one year.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    A pagination cursor returned by a previous call to this endpoint.
    Provide this cursor to retrieve the next set of results for the original query.
    If you do not provide the cursor, the call returns the first page of the results.
    """

    end_time: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp for the end of the reporting period, in RFC 3339 format.
    Inclusive. Default: The current time.
    """

    gift_card_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    If you provide a gift card ID, the endpoint returns activities that belong 
    to the specified gift card. Otherwise, the endpoint returns all gift card activities for 
    the seller.
    """

    limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    If you provide a limit value, the endpoint returns the specified number 
    of results (or less) per page. A maximum value is 100. The default value is 50.
    """

    location_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    If you provide a location ID, the endpoint returns gift card activities for that location. 
    Otherwise, the endpoint returns gift card activities for all locations.
    """

    sort_order: typing.Optional[str] = pydantic.Field(default=None)
    """
    The order in which the endpoint returns the activities, based on `created_at`.
    - `ASC` - Oldest to newest.
    - `DESC` - Newest to oldest (default).
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    If you provide a type, the endpoint returns gift card activities of this type. 
    Otherwise, the endpoint returns all types of gift card activities.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
