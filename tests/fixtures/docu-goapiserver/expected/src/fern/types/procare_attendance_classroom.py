

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .procare_attendance_student import ProcareAttendanceStudent


class ProcareAttendanceClassroom(UniversalBaseModel):
    """
    Procare Attendance Classroom.
    """

    room_id: str = pydantic.Field()
    """
    Room id.
    """

    room_name: str
    signed_in_count: int
    absent_count: int
    not_arrived_count: int
    students: typing.Optional[typing.List[ProcareAttendanceStudent]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
