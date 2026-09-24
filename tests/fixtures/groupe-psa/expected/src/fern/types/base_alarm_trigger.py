

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .base_alarm_trigger_position import BaseAlarmTriggerPosition
from .base_alarm_trigger_type import BaseAlarmTriggerType


class BaseAlarmTrigger(UniversalBaseModel):
    """
    Describe a vehicle alarm trigger.
    """

    type: BaseAlarmTriggerType = pydantic.Field()
    """
    Define the vehicle break-in type.
    """

    position: typing.Optional[BaseAlarmTriggerPosition] = None
    start_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="startAt"),
        pydantic.Field(alias="startAt", description="Time when the alarm triggering started."),
    ]
    """
    Time when the alarm triggering started.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
