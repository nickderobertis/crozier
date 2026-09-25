

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_status_whats_app_whatsapp_conversation import MessageStatusWhatsAppWhatsappConversation


class MessageStatusWhatsAppWhatsapp(UniversalBaseModel):
    """
    An object contining meta-data related to the WhatsApp message that triggered this callback. Only present for callbacks with a `status` of `delivered`.
    """

    conversation: typing.Optional[MessageStatusWhatsAppWhatsappConversation] = pydantic.Field(default=None)
    """
    An object contining data for the conversation to which the message relates.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
