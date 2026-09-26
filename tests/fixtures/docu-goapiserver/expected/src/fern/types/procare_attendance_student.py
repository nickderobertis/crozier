

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ProcareAttendanceStudent(UniversalBaseModel):
    """
    Procare Attendance Student.
    """

    student_id: str = pydantic.Field()
    """
    Student id.
    """

    first_name: str
    last_name: str
    state: str
    sign_in_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
