

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .channel_options_whatsapp import ChannelOptionsWhatsapp
from .location import Location


class SendMessageRequestTwoOne(Location, ChannelOptionsWhatsapp):
    text: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    The location to be sent in the message.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
