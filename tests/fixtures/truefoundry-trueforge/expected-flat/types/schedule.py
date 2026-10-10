

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .created_by_subject import CreatedBySubject
from .resource_name import ResourceName
from .schedule_manifest import ScheduleManifest


class Schedule(UniversalBaseModel):
    agent_name: ResourceName
    created_at: dt.datetime
    created_by_subject: CreatedBySubject
    id: str
    manifest: ScheduleManifest
    name: ResourceName
    updated_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
