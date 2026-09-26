

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .marimo_chatbot_send_prompt_input_messages_item_role import MarimoChatbotSendPromptInputMessagesItemRole


class MarimoChatbotSendPromptInputMessagesItem(UniversalBaseModel):
    id: str
    role: MarimoChatbotSendPromptInputMessagesItemRole
    content: typing.Optional[str] = None
    parts: typing.List[typing.Any]
    metadata: typing.Optional[typing.Any] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
