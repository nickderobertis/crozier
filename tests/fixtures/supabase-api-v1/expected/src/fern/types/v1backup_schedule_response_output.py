

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1BackupScheduleResponseOutput(UniversalBaseModel):
    schedule_for: str = pydantic.Field()
    """
    Time of day to schedule daily backups, in UTC. Format: HH:MM:SS.
    """

    updated_at: dt.datetime = pydantic.Field()
    """
    Timestamp of when the backup schedule was last updated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
