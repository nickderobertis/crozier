

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .invite_application_response import InviteApplicationResponse
from .invite_channel_response import InviteChannelResponse
from .invite_guild_response import InviteGuildResponse
from .invite_stage_instance_response import InviteStageInstanceResponse
from .invite_target_types import InviteTargetTypes
from .scheduled_event_response import ScheduledEventResponse
from .snowflake_type import SnowflakeType
from .user_response import UserResponse


class GuildInviteResponse(UniversalBaseModel):
    type: typing.Optional[int] = None
    code: str
    inviter: typing.Optional[UserResponse] = None
    max_age: typing.Optional[int] = None
    created_at: typing.Optional[dt.datetime] = None
    expires_at: typing.Optional[dt.datetime] = None
    is_contact: typing.Optional[bool] = None
    flags: typing.Optional[int] = None
    guild: typing.Optional[InviteGuildResponse] = None
    guild_id: typing.Optional[SnowflakeType] = None
    channel: typing.Optional[InviteChannelResponse] = None
    stage_instance: typing.Optional[InviteStageInstanceResponse] = None
    target_type: typing.Optional[InviteTargetTypes] = None
    target_user: typing.Optional[UserResponse] = None
    target_application: typing.Optional[InviteApplicationResponse] = None
    guild_scheduled_event: typing.Optional[ScheduledEventResponse] = None
    uses: typing.Optional[int] = None
    max_uses: typing.Optional[int] = None
    temporary: typing.Optional[bool] = None
    approximate_member_count: typing.Optional[int] = None
    approximate_presence_count: typing.Optional[int] = None
    is_nickname_changeable: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
