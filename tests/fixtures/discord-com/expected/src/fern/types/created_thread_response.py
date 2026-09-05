

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .snowflake_type import SnowflakeType
from .thread_member_response import ThreadMemberResponse
from .thread_metadata_response import ThreadMetadataResponse
from .video_quality_modes import VideoQualityModes


class CreatedThreadResponse(UniversalBaseModel):
    id: SnowflakeType
    type: int
    last_message_id: typing.Optional[SnowflakeType] = None
    flags: int
    last_pin_timestamp: typing.Optional[dt.datetime] = None
    guild_id: SnowflakeType
    name: str
    parent_id: typing.Optional[SnowflakeType] = None
    rate_limit_per_user: typing.Optional[int] = None
    bitrate: typing.Optional[int] = None
    user_limit: typing.Optional[int] = None
    rtc_region: typing.Optional[str] = None
    video_quality_mode: typing.Optional[VideoQualityModes] = None
    permissions: typing.Optional[str] = None
    owner_id: SnowflakeType
    thread_metadata: typing.Optional[ThreadMetadataResponse] = None
    message_count: int
    member_count: int
    total_message_sent: int
    applied_tags: typing.Optional[typing.List[SnowflakeType]] = None
    member: typing.Optional[ThreadMemberResponse] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
