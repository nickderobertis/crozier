

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Attendance(UniversalBaseModel):
    """
    A sparse row containing only the selected fields. Default fields: student_id, date, room_id, room_name, hours_attended.
    """

    attendance_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Attendance id.
    """

    student_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Student id.
    """

    date: typing.Optional[dt.date] = None
    room_id: typing.Optional[str] = None
    room_name: typing.Optional[str] = None
    hours_attended: typing.Optional[float] = None
    sign_in_time: typing.Optional[str] = pydantic.Field(default=None)
    """
    Local display time in h:mm AM/PM format, or an empty string when unavailable.
    """

    sign_out_time: typing.Optional[str] = pydantic.Field(default=None)
    """
    Local display time in h:mm AM/PM format, or an empty string when unavailable.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
