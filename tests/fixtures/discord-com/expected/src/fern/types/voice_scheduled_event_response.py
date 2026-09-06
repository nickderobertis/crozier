

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .entity_metadata_voice_response import EntityMetadataVoiceResponse
from .guild_scheduled_event_privacy_levels import GuildScheduledEventPrivacyLevels
from .guild_scheduled_event_statuses import GuildScheduledEventStatuses
from .scheduled_event_user_response import ScheduledEventUserResponse
from .snowflake_type import SnowflakeType
from .user_response import UserResponse


class VoiceScheduledEventResponse(UniversalBaseModel):
    id: SnowflakeType
    guild_id: SnowflakeType
    name: str
    description: typing.Optional[str] = None
    channel_id: typing.Optional[SnowflakeType] = None
    creator_id: typing.Optional[SnowflakeType] = None
    creator: typing.Optional[UserResponse] = None
    image: typing.Optional[str] = None
    scheduled_start_time: dt.datetime
    scheduled_end_time: typing.Optional[dt.datetime] = None
    status: GuildScheduledEventStatuses
    entity_type: int
    entity_id: typing.Optional[SnowflakeType] = None
    user_count: typing.Optional[int] = None
    privacy_level: GuildScheduledEventPrivacyLevels
    user_rsvp: typing.Optional[ScheduledEventUserResponse] = None
    entity_metadata: typing.Optional[EntityMetadataVoiceResponse] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
