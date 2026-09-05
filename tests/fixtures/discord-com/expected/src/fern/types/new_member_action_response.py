

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .new_member_action_type import NewMemberActionType
from .settings_emoji_response import SettingsEmojiResponse
from .snowflake_type import SnowflakeType


class NewMemberActionResponse(UniversalBaseModel):
    channel_id: SnowflakeType
    action_type: NewMemberActionType
    title: str
    description: str
    emoji: typing.Optional[SettingsEmojiResponse] = None
    icon: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
