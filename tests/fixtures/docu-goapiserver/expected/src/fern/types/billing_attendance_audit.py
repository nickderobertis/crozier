

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BillingAttendanceAudit(UniversalBaseModel):
    """
    Billing Attendance Audit.
    """

    date: dt.datetime
    student_id: str = pydantic.Field()
    """
    Student id.
    """

    room_id: str = pydantic.Field()
    """
    Room id.
    """

    hours_attended: float
    unpaid_day: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
