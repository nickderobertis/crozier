

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .shift_workday import ShiftWorkday
from .time_range import TimeRange


class ShiftFilter(UniversalBaseModel):
    """
    Defines a filter used in a search for `Shift` records. `AND` logic is
    used by Square's servers to apply each filter property specified.
    """

    employee_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Fetch shifts for the specified employees. DEPRECATED at version 2020-08-26. Use `team_member_ids` instead.
    """

    end: typing.Optional[TimeRange] = None
    location_ids: typing.List[str] = pydantic.Field()
    """
    Fetch shifts for the specified location.
    """

    start: typing.Optional[TimeRange] = None
    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Fetch a `Shift` instance by `Shift.status`.
    """

    team_member_ids: typing.List[str] = pydantic.Field()
    """
    Fetch shifts for the specified team members. Replaced `employee_ids` at version "2020-08-26".
    """

    workday: typing.Optional[ShiftWorkday] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
