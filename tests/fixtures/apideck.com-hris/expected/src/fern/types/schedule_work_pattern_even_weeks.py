

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ScheduleWorkPatternEvenWeeks(UniversalBaseModel):
    hours_friday: typing.Optional[float] = None
    hours_monday: typing.Optional[float] = None
    hours_saturday: typing.Optional[float] = None
    hours_sunday: typing.Optional[float] = None
    hours_thursday: typing.Optional[float] = None
    hours_tuesday: typing.Optional[float] = None
    hours_wednesday: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
