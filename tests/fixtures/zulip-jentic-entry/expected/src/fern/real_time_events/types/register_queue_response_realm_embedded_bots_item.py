

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.bot_configuration import BotConfiguration


class RegisterQueueResponseRealmEmbeddedBotsItem(UniversalBaseModel):
    """
    Object containing details of an embedded bot. Embedded bots are an experimental
    feature not enabled in production yet.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the bot.
    """

    config: typing.Optional[BotConfiguration] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
