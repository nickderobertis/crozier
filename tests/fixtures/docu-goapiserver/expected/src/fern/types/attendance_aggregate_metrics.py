

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AttendanceAggregateMetrics(UniversalBaseModel):
    attendance_days: typing.Optional[int] = None
    total_records: typing.Optional[int] = None
    sum_hours: typing.Optional[float] = None
    avg_hours: typing.Optional[float] = None
    distinct_students: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
