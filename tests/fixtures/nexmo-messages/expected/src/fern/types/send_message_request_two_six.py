

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .channel_options_whatsapp import ChannelOptionsWhatsapp
from .send_message_request_two_six_whatsapp import SendMessageRequestTwoSixWhatsapp
from .template import Template


class SendMessageRequestTwoSix(Template, ChannelOptionsWhatsapp):
    whatsapp: typing.Optional[SendMessageRequestTwoSixWhatsapp] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
