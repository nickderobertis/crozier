

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cron_schedule import CronSchedule


class AutoTriggerLogCleanupConfig(UniversalBaseModel):
    batch_size: typing.Optional[float] = None
    clean_invocation_logs: typing.Optional[bool] = None
    clear_older_than: float
    paused: typing.Optional[bool] = None
    schedule: CronSchedule
    timeout: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
