

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cron_expression import CronExpression
from .schedule_status import ScheduleStatus
from .timezone import Timezone


class ScheduleManifest(UniversalBaseModel):
    cron: CronExpression
    status: typing.Optional[ScheduleStatus] = None
    task: str = pydantic.Field()
    """
    First user message sent to the agent on every run.
    """

    timezone: typing.Optional[Timezone] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
