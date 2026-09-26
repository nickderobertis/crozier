

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .procare_attendance_classroom import ProcareAttendanceClassroom


class ClassroomAttendance(UniversalBaseModel):
    """
    Classroom Attendance.
    """

    date: str
    school_id: str = pydantic.Field()
    """
    School id.
    """

    school_time_zone: str
    last_synced_at: typing.Optional[dt.datetime] = None
    classrooms: typing.Optional[typing.List[ProcareAttendanceClassroom]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
