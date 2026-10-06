

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .base_calendar import BaseCalendar
from .date import Date
from .date1 import Date1
from .locale import Locale
from .time_zone import TimeZone


class GregorianCalendar(UniversalBaseModel):
    fields: typing.Optional[typing.List[int]] = None
    is_set: typing_extensions.Annotated[
        typing.Optional[typing.List[bool]], FieldMetadata(alias="isSet"), pydantic.Field(alias="isSet")
    ] = None
    time: typing.Optional[int] = None
    is_time_set: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isTimeSet"), pydantic.Field(alias="isTimeSet")
    ] = None
    are_fields_set: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="areFieldsSet"), pydantic.Field(alias="areFieldsSet")
    ] = None
    lenient: typing.Optional[bool] = None
    zone: typing.Optional[TimeZone] = None
    first_day_of_week: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="firstDayOfWeek"), pydantic.Field(alias="firstDayOfWeek")
    ] = None
    minimal_days_in_first_week: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="minimalDaysInFirstWeek"),
        pydantic.Field(alias="minimalDaysInFirstWeek"),
    ] = None
    next_stamp: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="nextStamp"), pydantic.Field(alias="nextStamp")
    ] = None
    serial_version_on_stream: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="serialVersionOnStream"),
        pydantic.Field(alias="serialVersionOnStream"),
    ] = None
    time_in_millis: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="timeInMillis"), pydantic.Field(alias="timeInMillis")
    ] = None
    set_state_fields: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="setStateFields"), pydantic.Field(alias="setStateFields")
    ] = None
    fields_computed: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="fieldsComputed"), pydantic.Field(alias="fieldsComputed")
    ] = None
    fields_normalized: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="fieldsNormalized"), pydantic.Field(alias="fieldsNormalized")
    ] = None
    partially_normalized: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="partiallyNormalized"), pydantic.Field(alias="partiallyNormalized")
    ] = None
    fully_normalized: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="fullyNormalized"), pydantic.Field(alias="fullyNormalized")
    ] = None
    zone_shared: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="zoneShared"), pydantic.Field(alias="zoneShared")
    ] = None
    week_count_data: typing_extensions.Annotated[
        typing.Optional[Locale], FieldMetadata(alias="weekCountData"), pydantic.Field(alias="weekCountData")
    ] = None
    gregorian_cutover: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="gregorianCutover"), pydantic.Field(alias="gregorianCutover")
    ] = None
    gregorian_change: typing_extensions.Annotated[
        typing.Optional[Date], FieldMetadata(alias="gregorianChange"), pydantic.Field(alias="gregorianChange")
    ] = None
    calendar_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="calendarType"), pydantic.Field(alias="calendarType")
    ] = None
    year_offset_in_millis: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="yearOffsetInMillis"), pydantic.Field(alias="yearOffsetInMillis")
    ] = None
    time_zone: typing_extensions.Annotated[
        typing.Optional[TimeZone], FieldMetadata(alias="timeZone"), pydantic.Field(alias="timeZone")
    ] = None
    week_date_supported: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="weekDateSupported"), pydantic.Field(alias="weekDateSupported")
    ] = None
    week_year: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="weekYear"), pydantic.Field(alias="weekYear")
    ] = None
    weeks_in_week_year: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="weeksInWeekYear"), pydantic.Field(alias="weeksInWeekYear")
    ] = None
    normalized_calendar: typing_extensions.Annotated[
        typing.Optional["GregorianCalendar"],
        FieldMetadata(alias="normalizedCalendar"),
        pydantic.Field(alias="normalizedCalendar"),
    ] = None
    cutover_calendar_system: typing_extensions.Annotated[
        typing.Optional[BaseCalendar],
        FieldMetadata(alias="cutoverCalendarSystem"),
        pydantic.Field(alias="cutoverCalendarSystem"),
    ] = None
    invalid_week1: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="invalidWeek1"), pydantic.Field(alias="invalidWeek1")
    ] = None
    last_julian_date: typing_extensions.Annotated[
        typing.Optional[Date1], FieldMetadata(alias="lastJulianDate"), pydantic.Field(alias="lastJulianDate")
    ] = None
    current_fixed_date: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="currentFixedDate"), pydantic.Field(alias="currentFixedDate")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(GregorianCalendar)
