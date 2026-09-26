

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .marimo_chatbot_send_prompt_input_config import MarimoChatbotSendPromptInputConfig
from .marimo_chatbot_send_prompt_input_messages_item import MarimoChatbotSendPromptInputMessagesItem


class MarimoChatbotSendPromptInput(UniversalBaseModel):
    request_id: str
    messages: typing.List[MarimoChatbotSendPromptInputMessagesItem]
    config: MarimoChatbotSendPromptInputConfig

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
