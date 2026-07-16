

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .break_ import Break
from .shift_wage import ShiftWage


class Shift(UniversalBaseModel):
    """
    A record of the hourly rate, start, and end times for a single work shift
    for an employee. This might include a record of the start and end times for breaks
    taken during the shift.
    """

    breaks: typing.Optional[typing.List[Break]] = pydantic.Field(default=None)
    """
    A list of all the paid or unpaid breaks that were taken during this shift.
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    A read-only timestamp in RFC 3339 format; presented in UTC.
    """

    employee_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the employee this shift belongs to. DEPRECATED at version 2020-08-26. Use `team_member_id` instead.
    """

    end_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    RFC 3339; shifted to the timezone + offset. Precision up to the minute is
    respected; seconds are truncated.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The UUID for this object.
    """

    location_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the location this shift occurred at. The location should be based on
    where the employee clocked in.
    """

    start_at: str = pydantic.Field()
    """
    RFC 3339; shifted to the location timezone + offset. Precision up to the
    minute is respected; seconds are truncated.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Describes the working state of the current `Shift`.
    """

    team_member_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the team member this shift belongs to. Replaced `employee_id` at version "2020-08-26".
    """

    timezone: typing.Optional[str] = pydantic.Field(default=None)
    """
    The read-only convenience value that is calculated from the location based
    on the `location_id`. Format: the IANA timezone database identifier for the
    location timezone.
    """

    updated_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    A read-only timestamp in RFC 3339 format; presented in UTC.
    """

    version: typing.Optional[int] = pydantic.Field(default=None)
    """
    Used for resolving concurrency issues. The request fails if the version
    provided does not match the server version at the time of the request. If not provided,
    Square executes a blind write; potentially overwriting data from another
    write.
    """

    wage: typing.Optional[ShiftWage] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
