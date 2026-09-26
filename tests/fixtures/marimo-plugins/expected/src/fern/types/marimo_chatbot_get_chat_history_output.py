

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .marimo_chatbot_get_chat_history_output_messages_item import MarimoChatbotGetChatHistoryOutputMessagesItem


class MarimoChatbotGetChatHistoryOutput(UniversalBaseModel):
    messages: typing.List[MarimoChatbotGetChatHistoryOutputMessagesItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
