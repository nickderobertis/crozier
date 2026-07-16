

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .connection_schedule_time_unit import ConnectionScheduleTimeUnit


class ConnectionSchedule(UniversalBaseModel):
    """
    if null, then no schedule is set.
    """

    time_unit: typing_extensions.Annotated[
        ConnectionScheduleTimeUnit, FieldMetadata(alias="timeUnit"), pydantic.Field(alias="timeUnit")
    ]
    units: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
