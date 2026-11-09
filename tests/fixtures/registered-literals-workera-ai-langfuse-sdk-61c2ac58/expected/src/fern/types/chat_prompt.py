

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_prompt import BasePrompt
from .chat_message import ChatMessage


class ChatPrompt(BasePrompt):
    prompt: typing.List[ChatMessage]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
