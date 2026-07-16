

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .date_range import DateRange


class ShiftWorkday(UniversalBaseModel):
    """
    A `Shift` search query filter parameter that sets a range of days that
    a `Shift` must start or end in before passing the filter condition.
    """

    date_range: typing.Optional[DateRange] = None
    default_timezone: typing.Optional[str] = pydantic.Field(default=None)
    """
    Location-specific timezones convert workdays to datetime filters.
    Every location included in the query must have a timezone or this field
    must be provided as a fallback. Format: the IANA timezone database
    identifier for the relevant timezone.
    """

    match_shifts_by: typing.Optional[str] = pydantic.Field(default=None)
    """
    The strategy on which the dates are applied.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
