

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BusinessHoursPeriod(UniversalBaseModel):
    """
    Represents a period of time during which a business location is open.
    """

    day_of_week: typing.Optional[str] = pydantic.Field(default=None)
    """
    The day of week for this time period.
    """

    end_local_time: typing.Optional[str] = pydantic.Field(default=None)
    """
    The end time of a business hours period, specified in local time using partial-time
    RFC 3339 format.
    """

    start_local_time: typing.Optional[str] = pydantic.Field(default=None)
    """
    The start time of a business hours period, specified in local time using partial-time
    RFC 3339 format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
