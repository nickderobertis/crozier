

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .calendar_event_event_type import CalendarEventEventType
from .links import Links
from .recurring_event_details import RecurringEventDetails


class CalendarEvent(UniversalBaseModel):
    id: float
    company_id: typing_extensions.Annotated[float, FieldMetadata(alias="companyId"), pydantic.Field(alias="companyId")]
    user_id: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="userId"), pydantic.Field(alias="userId")
    ] = None
    user_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="userName"), pydantic.Field(alias="userName")
    ] = None
    group_id: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="groupId"), pydantic.Field(alias="groupId")
    ] = None
    title: str
    description: typing.Optional[str] = None
    event_type: typing_extensions.Annotated[
        CalendarEventEventType, FieldMetadata(alias="eventType"), pydantic.Field(alias="eventType")
    ]
    job_phase_id: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="jobPhaseId"), pydantic.Field(alias="jobPhaseId")
    ] = None
    job_id: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="jobId"), pydantic.Field(alias="jobId")
    ] = None
    start_time: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="startTime"),
        pydantic.Field(
            alias="startTime",
            description="The start time of the calendar event in ISO string format in 15 minute intervals",
        ),
    ]
    """
    The start time of the calendar event in ISO string format in 15 minute intervals
    """

    end_time: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="endTime"),
        pydantic.Field(
            alias="endTime",
            description="The end time of the calendar event in ISO string format in 15 minute intervals",
        ),
    ]
    """
    The end time of the calendar event in ISO string format in 15 minute intervals
    """

    is_active: typing_extensions.Annotated[bool, FieldMetadata(alias="isActive"), pydantic.Field(alias="isActive")]
    is_all_day: typing_extensions.Annotated[bool, FieldMetadata(alias="isAllDay"), pydantic.Field(alias="isAllDay")]
    is_recurring: typing_extensions.Annotated[
        bool, FieldMetadata(alias="isRecurring"), pydantic.Field(alias="isRecurring")
    ]
    recurring_event_details: typing_extensions.Annotated[
        typing.Optional[RecurringEventDetails],
        FieldMetadata(alias="recurringEventDetails"),
        pydantic.Field(alias="recurringEventDetails"),
    ] = None
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    links: typing.List[Links]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
