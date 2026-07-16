

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListCashDrawerShiftsRequest(UniversalBaseModel):
    """ """

    begin_time: typing.Optional[str] = pydantic.Field(default=None)
    """
    The inclusive start time of the query on opened_at, in ISO 8601 format.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    Opaque cursor for fetching the next page of results.
    """

    end_time: typing.Optional[str] = pydantic.Field(default=None)
    """
    The exclusive end date of the query on opened_at, in ISO 8601 format.
    """

    limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of cash drawer shift events in a page of results (200 by
    default, 1000 max).
    """

    location_id: str = pydantic.Field()
    """
    The ID of the location to query for a list of cash drawer shifts.
    """

    sort_order: typing.Optional[str] = pydantic.Field(default=None)
    """
    The order in which cash drawer shifts are listed in the response,
    based on their opened_at field. Default value: ASC
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
