

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .new_member_action_response import NewMemberActionResponse
from .resource_channel_response import ResourceChannelResponse
from .snowflake_type import SnowflakeType
from .welcome_message_response import WelcomeMessageResponse


class GuildHomeSettingsResponse(UniversalBaseModel):
    guild_id: SnowflakeType
    enabled: bool
    welcome_message: typing.Optional[WelcomeMessageResponse] = None
    new_member_actions: typing.Optional[typing.List[typing.Optional[NewMemberActionResponse]]] = None
    resource_channels: typing.Optional[typing.List[typing.Optional[ResourceChannelResponse]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
