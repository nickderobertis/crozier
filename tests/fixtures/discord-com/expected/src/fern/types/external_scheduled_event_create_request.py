

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .entity_metadata_external import EntityMetadataExternal
from .guild_scheduled_event_privacy_levels import GuildScheduledEventPrivacyLevels
from .snowflake_type import SnowflakeType


class ExternalScheduledEventCreateRequest(UniversalBaseModel):
    name: str
    description: typing.Optional[str] = None
    image: typing.Optional[str] = None
    scheduled_start_time: dt.datetime
    scheduled_end_time: typing.Optional[dt.datetime] = None
    privacy_level: GuildScheduledEventPrivacyLevels
    entity_type: int
    channel_id: typing.Optional[SnowflakeType] = None
    entity_metadata: EntityMetadataExternal

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
