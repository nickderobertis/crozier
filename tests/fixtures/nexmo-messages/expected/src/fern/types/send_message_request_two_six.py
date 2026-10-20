

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .channel_options_whatsapp_channel import ChannelOptionsWhatsappChannel
from .from_number import FromNumber
from .send_message_request_two_six_whatsapp import SendMessageRequestTwoSixWhatsapp
from .template import Template
from .to_number import ToNumber


class SendMessageRequestTwoSix(Template):
    to: ToNumber
    from_: typing_extensions.Annotated[FromNumber, FieldMetadata(alias="from"), pydantic.Field(alias="from")]
    channel: ChannelOptionsWhatsappChannel = pydantic.Field()
    """
    The channel to send to. You must provide `whatsapp` in this field
    """

    whatsapp: typing.Optional[SendMessageRequestTwoSixWhatsapp] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
