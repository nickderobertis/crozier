

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .created_by_subject import CreatedBySubject
from .schedule_run_status import ScheduleRunStatus


class ScheduleRun(UniversalBaseModel):
    created_at: dt.datetime
    created_by_subject: CreatedBySubject
    id: str
    name: str
    schedule_id: str
    scheduled_for: dt.datetime
    status: ScheduleRunStatus
    triggered_at: typing.Optional[dt.datetime] = None
    updated_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
