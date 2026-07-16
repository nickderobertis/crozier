

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .segment_filter import SegmentFilter
from .time_range import TimeRange


class SearchAvailabilityFilter(UniversalBaseModel):
    """
    A query filter to search for availabilities by.
    """

    booking_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The query expression to search for availabilities for an existing booking by matching the specified `booking_id` value.
    This is commonly used to reschedule an appointment.
    If this expression is specified, the `location_id` and `segment_filters` expressions are not allowed.
    """

    location_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The query expression to search for availabilities matching the specified seller location IDs.
    This query expression is not applicable when `booking_id` is present.
    """

    segment_filters: typing.Optional[typing.List[SegmentFilter]] = pydantic.Field(default=None)
    """
    The list of segment filters to apply. A query with `n` segment filters returns availabilities with `n` segments per
    availability. It is not applicable when `booking_id` is present.
    """

    start_at_range: TimeRange

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
