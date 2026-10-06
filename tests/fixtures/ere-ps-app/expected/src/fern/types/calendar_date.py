

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .locale import Locale
from .time_zone import TimeZone


class CalendarDate(UniversalBaseModel):
    era: typing.Optional["Era"] = None
    year: typing.Optional[int] = None
    month: typing.Optional[int] = None
    day_of_month: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="dayOfMonth"), pydantic.Field(alias="dayOfMonth")
    ] = None
    day_of_week: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="dayOfWeek"), pydantic.Field(alias="dayOfWeek")
    ] = None
    leap_year: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="leapYear"), pydantic.Field(alias="leapYear")
    ] = None
    hours: typing.Optional[int] = None
    minutes: typing.Optional[int] = None
    seconds: typing.Optional[int] = None
    millis: typing.Optional[int] = None
    fraction: typing.Optional[int] = None
    normalized: typing.Optional[bool] = None
    zoneinfo: typing.Optional[TimeZone] = None
    zone_offset: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="zoneOffset"), pydantic.Field(alias="zoneOffset")
    ] = None
    daylight_saving: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="daylightSaving"), pydantic.Field(alias="daylightSaving")
    ] = None
    force_standard_time: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="forceStandardTime"), pydantic.Field(alias="forceStandardTime")
    ] = None
    locale: typing.Optional[Locale] = None
    time_of_day: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="timeOfDay"), pydantic.Field(alias="timeOfDay")
    ] = None
    standard_time: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="standardTime"), pydantic.Field(alias="standardTime")
    ] = None
    daylight_time: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="daylightTime"), pydantic.Field(alias="daylightTime")
    ] = None
    zone: typing.Optional[TimeZone] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .era import Era

update_forward_refs(CalendarDate, Era=Era)
