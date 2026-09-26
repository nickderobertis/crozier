

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_status_whats_app_whatsapp_conversation_origin import MessageStatusWhatsAppWhatsappConversationOrigin


class MessageStatusWhatsAppWhatsappConversation(UniversalBaseModel):
    """
    An object contining data for the conversation to which the message relates.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the conversation.
    """

    origin: typing.Optional[MessageStatusWhatsAppWhatsappConversationOrigin] = pydantic.Field(default=None)
    """
    An object contining data related to the origin of the conversation.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
