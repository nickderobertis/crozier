

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .campaign_block_content_type import CampaignBlockContentType
from .campaign_block_type import CampaignBlockType


class CampaignBlock(UniversalBaseModel):
    id: str
    name: str
    content_type: typing_extensions.Annotated[
        CampaignBlockContentType, FieldMetadata(alias="contentType"), pydantic.Field(alias="contentType")
    ]
    content_id: typing_extensions.Annotated[str, FieldMetadata(alias="contentId"), pydantic.Field(alias="contentId")]
    content_revision: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="contentRevision"), pydantic.Field(alias="contentRevision")
    ] = None
    priority: int
    type: CampaignBlockType
    timezone: str
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
    enabled: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
