

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .snowflake_type import SnowflakeType
from .widget_activity import WidgetActivity
from .widget_user_discriminator import WidgetUserDiscriminator


class WidgetMember(UniversalBaseModel):
    id: str
    username: str
    discriminator: WidgetUserDiscriminator
    avatar: typing.Optional[typing.Any] = None
    status: str
    avatar_url: str
    activity: typing.Optional[WidgetActivity] = None
    deaf: typing.Optional[bool] = None
    mute: typing.Optional[bool] = None
    self_deaf: typing.Optional[bool] = None
    self_mute: typing.Optional[bool] = None
    suppress: typing.Optional[bool] = None
    channel_id: typing.Optional[SnowflakeType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
