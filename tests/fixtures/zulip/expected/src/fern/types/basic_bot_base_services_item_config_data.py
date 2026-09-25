

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bot_configuration import BotConfiguration


class BasicBotBaseServicesItemConfigData(UniversalBaseModel):
    """
    When the bot is an embedded bot.
    """

    service_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the bot.
    """

    config_data: typing.Optional[BotConfiguration] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
