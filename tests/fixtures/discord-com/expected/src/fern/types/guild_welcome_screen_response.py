

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .guild_welcome_screen_channel_response import GuildWelcomeScreenChannelResponse


class GuildWelcomeScreenResponse(UniversalBaseModel):
    description: typing.Optional[str] = None
    welcome_channels: typing.List[GuildWelcomeScreenChannelResponse]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
