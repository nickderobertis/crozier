

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .snowflake_type import SnowflakeType
from .stage_instances_privacy_levels import StageInstancesPrivacyLevels


class StageInstanceResponse(UniversalBaseModel):
    guild_id: SnowflakeType
    channel_id: SnowflakeType
    topic: str
    privacy_level: StageInstancesPrivacyLevels
    id: SnowflakeType
    discoverable_disabled: typing.Optional[bool] = None
    guild_scheduled_event_id: typing.Optional[SnowflakeType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
