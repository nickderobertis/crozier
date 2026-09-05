

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .entity_metadata_voice import EntityMetadataVoice
from .guild_scheduled_event_privacy_levels import GuildScheduledEventPrivacyLevels
from .guild_scheduled_event_statuses import GuildScheduledEventStatuses
from .snowflake_type import SnowflakeType


class VoiceScheduledEventPatchRequestPartial(UniversalBaseModel):
    status: typing.Optional[GuildScheduledEventStatuses] = None
    name: typing.Optional[str] = None
    description: typing.Optional[str] = None
    image: typing.Optional[str] = None
    scheduled_start_time: typing.Optional[dt.datetime] = None
    scheduled_end_time: typing.Optional[dt.datetime] = None
    entity_type: typing.Optional[int] = None
    privacy_level: typing.Optional[GuildScheduledEventPrivacyLevels] = None
    channel_id: typing.Optional[SnowflakeType] = None
    entity_metadata: typing.Optional[EntityMetadataVoice] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
