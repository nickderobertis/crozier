

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .guild_template_snapshot_response import GuildTemplateSnapshotResponse
from .snowflake_type import SnowflakeType
from .user_response import UserResponse


class GuildTemplateResponse(UniversalBaseModel):
    code: str
    name: str
    description: typing.Optional[str] = None
    usage_count: int
    creator_id: SnowflakeType
    creator: typing.Optional[UserResponse] = None
    created_at: dt.datetime
    updated_at: dt.datetime
    source_guild_id: SnowflakeType
    serialized_source_guild: GuildTemplateSnapshotResponse
    is_dirty: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
