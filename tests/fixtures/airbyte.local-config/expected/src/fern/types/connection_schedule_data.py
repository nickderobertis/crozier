

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .connection_schedule_data_basic_schedule import ConnectionScheduleDataBasicSchedule
from .connection_schedule_data_cron import ConnectionScheduleDataCron


class ConnectionScheduleData(UniversalBaseModel):
    """
    schedule for when the the connection should run, per the schedule type
    """

    basic_schedule: typing_extensions.Annotated[
        typing.Optional[ConnectionScheduleDataBasicSchedule], FieldMetadata(alias="basicSchedule")
    ] = None
    cron: typing.Optional[ConnectionScheduleDataCron] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
