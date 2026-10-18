

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .channel_options_whatsapp_channel import ChannelOptionsWhatsappChannel
from .from_number import FromNumber
from .location import Location
from .to_number import ToNumber


class SendMessageRequestTwoOne(Location):
    to: ToNumber
    from_: typing_extensions.Annotated[FromNumber, FieldMetadata(alias="from"), pydantic.Field(alias="from")]
    channel: ChannelOptionsWhatsappChannel = pydantic.Field()
    """
    The channel to send to. You must provide `whatsapp` in this field
    """

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
