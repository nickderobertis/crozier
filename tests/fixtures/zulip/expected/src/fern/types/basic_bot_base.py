

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .basic_bot_base_services_item import BasicBotBaseServicesItem


class BasicBotBase(UniversalBaseModel):
    user_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The user ID of the bot.
    """

    default_sending_stream: typing.Optional[str] = pydantic.Field(default=None)
    """
    The default sending channel of the bot. If `null`, the bot doesn't
    have a default sending channel.
    """

    default_events_register_stream: typing.Optional[str] = pydantic.Field(default=None)
    """
    The default channel for which the bot receives events/register data.
    If `null`, the bot doesn't have such a default channel.
    """

    default_all_public_streams: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the bot can send messages to all channels by default.
    """

    services: typing.Optional[typing.List[BasicBotBaseServicesItem]] = pydantic.Field(default=None)
    """
    An array containing extra configuration fields only relevant for
    outgoing webhook bots and embedded bots. This is always a single-element
    array.
    
    We consider this part of the Zulip API to be unstable; it is used only
    for UI elements for administering bots and is likely to change.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
