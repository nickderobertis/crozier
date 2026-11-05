

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .display_control_action import DisplayControlAction
from .manifest_schedule_type import ManifestScheduleType


class ManifestSchedule(UniversalBaseModel):
    id: str
    playlist_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="playlistId"), pydantic.Field(alias="playlistId")
    ] = None
    layout_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="layoutId"), pydantic.Field(alias="layoutId")
    ] = None
    display_action: typing_extensions.Annotated[
        typing.Optional[DisplayControlAction],
        FieldMetadata(alias="displayAction"),
        pydantic.Field(alias="displayAction"),
    ] = None
    type: ManifestScheduleType
    timezone: str
    priority: int
    specificity: int
    start_date: typing_extensions.Annotated[
        typing.Optional[dt.date], FieldMetadata(alias="startDate"), pydantic.Field(alias="startDate")
    ] = None
    end_date: typing_extensions.Annotated[
        typing.Optional[dt.date], FieldMetadata(alias="endDate"), pydantic.Field(alias="endDate")
    ] = None
    one_time_start: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="oneTimeStart"), pydantic.Field(alias="oneTimeStart")
    ] = None
    one_time_end: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="oneTimeEnd"), pydantic.Field(alias="oneTimeEnd")
    ] = None
    daily_start: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="dailyStart"), pydantic.Field(alias="dailyStart")
    ] = None
    daily_end: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="dailyEnd"), pydantic.Field(alias="dailyEnd")
    ] = None
    days_of_week: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="daysOfWeek"), pydantic.Field(alias="daysOfWeek")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
